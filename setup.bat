@echo off

echo Installing Python dependencies...

python -m pip install --upgrade pip
pip install -r requirements.txt

echo.
echo Setup Complete!
pause
