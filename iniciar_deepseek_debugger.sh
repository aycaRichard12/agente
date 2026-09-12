#!/bin/bash

# Título de la terminal
echo -ne "\033]0;DeepSeek Debugger GUI\007"

# Cambiar al directorio donde está este script
cd "$(dirname "$0")" || exit 1

echo "========================================================"
echo "        Iniciando DeepSeek Debugger GUI"
echo "========================================================"
echo

# 1. Verificar si el entorno virtual existe
if [ ! -f "venv/bin/python" ]; then
    echo "[INFO] Creando el entorno virtual venv..."

    python3 -m venv venv

    if [ $? -ne 0 ]; then
        echo "[ERROR] No se pudo crear el entorno virtual."
        echo "Asegúrate de tener Python 3 instalado."
        echo
        read -p "Presiona Enter para salir..."
        exit 1
    fi

    echo "[INFO] Instalando dependencias desde requirements.txt..."

    venv/bin/python -m pip install -r requirements.txt

    if [ $? -ne 0 ]; then
        echo "[ERROR] Error al instalar dependencias."
        echo
        read -p "Presiona Enter para salir..."
        exit 1
    fi
fi

# 2. Ejecutar la aplicación usando Python del entorno virtual
echo "[INFO] Lanzando la interfaz gráfica..."

venv/bin/python main.py

if [ $? -ne 0 ]; then
    echo "[ERROR] Ocurrió un error al ejecutar la aplicación."
    echo
    read -p "Presiona Enter para salir..."
    exit 1
fi

echo "[INFO] Aplicación finalizada correctamente."