# 📦 DeepSeek Code Packager (Modular Architecture)

**DeepSeek Code Packager** es una herramienta de escritorio desacoplada y modular diseñada para empaquetar código fuente de proyectos en documentos estructurados `.md` (Markdown) o `.txt` (Texto Plano), optimizada para subir y analizar manualmente en el chat web de **DeepSeek**, **ChatGPT** o **Claude**.

---

## 🏗️ Arquitectura del Proyecto

El proyecto sigue el principio de separación de responsabilidades (*Separation of Concerns*), manteniendo la lógica de escaneo, modelos de datos, lectura de archivos y generación de prompts completamente independientes de la interfaz gráfica.

```
deepseek_debugger/
│
├── main.py                         # Punto de entrada principal
├── deepseek_gui.py                 # Wrapper ejecutable de compatibilidad
│
├── app/                            # Módulo principal del sistema
│   ├── __init__.py
│   │
│   ├── gui/                        # Capa de Interfaz Gráfica (Tkinter/ttk)
│   │   ├── __init__.py
│   │   ├── main_window.py          # Ventana principal y control de eventos
│   │   ├── file_tree.py            # Componente de árbol con checkboxes
│   │   └── dialogs.py              # Envoltorios de diálogos y alertas
│   │
│   ├── core/                       # Lógica central del sistema
│   │   ├── __init__.py
│   │   ├── project_scanner.py      # Escaneo recursivo de directorios
│   │   ├── file_selector.py        # Gestor de estado de selección (1 carpeta + N archivos)
│   │   ├── file_reader.py          # Lectura segura y numeración de líneas
│   │   └── project_structure.py    # Generador de estructura en árbol ASCII
│   │
│   ├── generators/                 # Generadores de documentos
│   │   ├── __init__.py
│   │   ├── markdown_generator.py   # Formateador en formato Markdown (.md)
│   │   ├── text_generator.py       # Formateador en texto plano (.txt)
│   │   └── prompt_generator.py     # Orquestador principal de generación
│   │
│   ├── models/                     # Modelos de datos
│   │   ├── __init__.py
│   │   └── project.py              # Clases de datos (ProjectSelection, ExportConfig)
│   │
│   └── utils/                      # Utilidades del sistema
│       ├── __init__.py
│       ├── file_utils.py           # Lectura/Escritura I/O y portapapeles
│       └── path_utils.py           # Resolución de rutas relativas y absolutas
│
├── output/                         # Carpeta por defecto para exportaciones
├── requirements.txt
├── ejecutar.bat                    # Script de inicio silencioso en Windows
├── ejecutar_con_consola.bat        # Script de inicio en modo consola/debug
└── README.md
```

---

## 🚀 Características Principales

1. **Sin dependencias de API ni llamadas HTTP**: Funciona 100% offline y sin necesidad de claves de API.
2. **Selección Flexible de Archivos**:
   - **Máximo 1 Carpeta de Proyecto**: Al seleccionar una nueva carpeta, se reemplaza la anterior.
   - **N Archivos Individuales**: Permite sumar cualquier cantidad de archivos sueltos desde distintas ubicaciones.
   - Soporta combinaciones: `1 Carpeta + N Archivos`, `Solo 1 Carpeta`, o `Solo N Archivos`.
3. **Exclusiones Dinámicas Configurables**:
   - Omite por defecto `.git`, `node_modules`, `__pycache__`, `venv`, `.venv`, `dist`, `build`, `.idea`, `.vscode`.
   - Permite editar la lista de directorios excluidos directamente desde la interfaz.
4. **Formateo para LLM Web Chat**:
   - Agrega árbol de directorio de la carpeta del proyecto.
   - Formatea el código con números de línea (`1 | código...`).
   - Permite copiar directamente al portapapeles o guardar el documento generado en la carpeta `output/` o donde desees.

---

## 💻 Ejecución

### Desde Scripts `.bat` (Windows):
- Haz doble clic en `ejecutar.bat` (Modo Ventana).
- O en `ejecutar_con_consola.bat` (Modo Consola / Debug).

### Desde la Consola de Comandos (Python):
```bash
python main.py
```
O usando el wrapper de compatibilidad:
```bash
python deepseek_gui.py
```
