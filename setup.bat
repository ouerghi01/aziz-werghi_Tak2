@echo off

REM Create virtual environment
python -m venv .venv

REM Activate virtual environment
call .venv\Scripts\activate

REM Install dependencies
pip install -r requirements.txt

echo Setup complete. Virtual environment created and dependencies installed.
