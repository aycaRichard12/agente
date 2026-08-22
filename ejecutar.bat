@echo off
title DeepSeek Debugger GUI
cd /d "%~dp0"

echo ========================================================
echo         Iniciando DeepSeek Debugger GUI
echo ========================================================
echo.

:: 1. Verificar si el entorno virtual existe
if not exist "%~dp0venv\Scripts\python.exe" (
    echo [INFO] Creando el entorno virtual venv...
    python -m venv "%~dp0venv"
    if errorlevel 1 (
        echo [ERROR] No se pudo crear el entorno virtual.
        echo Asegurate de tener Python instalado y agregado al PATH.
        echo.
        pause
        exit /b 1
    )
    echo [INFO] Instalando dependencias desde requirements.txt...
    "%~dp0venv\Scripts\python.exe" -m pip install -r "%~dp0requirements.txt"
    if errorlevel 1 (
        echo [ERROR] Error al instalar dependencias.
        echo.
        pause
        exit /b 1
    )
)

:: 2. Ejecutar la aplicacion usando el Python del entorno virtual
echo [INFO] Lanzando la interfaz grafica...
start "" "%~dp0venv\Scripts\pythonw.exe" "%~dp0deepseek_gui.py"

if errorlevel 1 (
    echo [ERROR] Ocurrio un error al lanzar la aplicacion.
    echo.
    pause
    exit /b 1
)

echo [INFO] Aplicacion iniciada correctamente.
