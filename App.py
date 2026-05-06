y=GROQ_API_KEY,
    )

    docs = text_splitter.split_documents(documents)

    # Create Chroma Vector Store
    vector_store = Chroma.from_documents(
        documents=docs,
        embedding=embeddings,
        persist_directory="chroma_db"
    )

    retriever = vector_store.as_retriever(search_kwargs={"k": 3})

    # Conversational Memory
    memory = ConversationBufferMemory(
        memory_key="chat_history",
        return_messages=True
    )

    # Create QA Chain
    qa_chain = ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=retriever,
        memory=memory
    )


# Chat Start Event
@cl.on_chat_start
async def start():
    await cl.Message(
        content="Upload a PDF file to start chatting with your document."
    ).send()


# Handle File Upload
@cl.on_message
async def main(message: cl.Message):
    global qa_chain

    # If user uploads a PDF
    if message.elements:
        for element in message.elements:
            if "pdf" in element.mime:
                file_path = element.path

                await cl.Message(
                    content="Processing PDF... Please wait."
                ).send()

                process_pdf(file_path)

                await cl.Message(
                    content="PDF processed successfully. Ask your questions now!"
                ).send()
                return

    # If user asks question
    if qa_chain:
        response = qa_chain.invoke({"question": message.content})

        answer = response["answer"]

        await cl.Message(content=answer).send()

    else:
        await cl.Message(
            content="Please upload a PDF first."
        ).send()
      
