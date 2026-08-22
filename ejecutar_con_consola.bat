@echo off
title DeepSeek Debugger GUI - Modo Consola
cd /d "%~dp0"

echo ========================================================
echo         Ejecutando en Modo Consola - Debug
echo ========================================================
echo.

if not exist "%~dp0venv\Scripts\python.exe" (
    echo [INFO] Creando el entorno virtual venv...
    python -m venv "%~dp0venv"
    echo [INFO] Instalando dependencias...
    "%~dp0venv\Scripts\python.exe" -m pip install -r "%~dp0requirements.txt"
)

echo [INFO] Iniciando main.py...
echo.
"%~dp0venv\Scripts\python.exe" "%~dp0main.py"

echo.
echo ========================================================
echo La aplicacion se ha cerrado. Presiona cualquier tecla para salir.
echo ========================================================
pause
