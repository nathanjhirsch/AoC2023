@echo off
set /p "id=Name: "
mkdir %id%
cd %id%
echo.> main.py
python -m venv .venv