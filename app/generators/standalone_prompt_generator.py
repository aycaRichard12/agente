"""Generates standalone professional prompt deepseek_prompt.md with structured DeepSeek response template."""
from app.models.analysis_types import get_analysis_profile


def generate_standalone_prompt(problem_desc: str = "", analysis_type: str = "Detect errors") -> str:
    """
    Generates a professional copy-paste prompt instructing DeepSeek:
    1. How to analyze the attached project context files according to the selected AnalysisProfile.
    2. Defines the exact objective, focus, priorities, and expected outcome.
    3. What exact structured markdown response format to return.
    """
    problem_text = problem_desc.strip() if problem_desc.strip() else "[Describe aquí el problema o requerimiento que deseas abordar]"
    profile = get_analysis_profile(analysis_type)

    prompt = f"""# PROMPT PROFESIONAL PARA DEEPSEEK WEB CHAT

> **Instrucción para el usuario:** Copia este texto y pégalo directamente en el chat de DeepSeek junto con los archivos adjuntos (`deepseek_project_context.md` o `deepseek_project_context.txt`).

==============================================================
TIPO DE ANÁLISIS SELECCIONADO / SELECTED ANALYSIS PROFILE: {profile.icon} {profile.name}
==============================================================
• OBJETIVO: {profile.objective}
• ENFOQUE: {profile.focus}
• PRIORIDADES: {profile.priorities}
• RESULTADO ESPERADO: {profile.expected_outcome}

⚠️ REGLA DE CONCRECIÓN TÉCNICA Y ACCIÓN:
{profile.response_instructions}

==============================================================
REPORTED PROBLEM OR GOAL / PROBLEMA REPORTADO U OBJETIVO
==============================================================
{problem_text}

==============================================================
PROJECT CONTEXT / CONTEXTO E INSTRUCCIONES DEL PROYECTO
==============================================================
Hola DeepSeek. Te adjunto el contexto completo de mi proyecto de software para su análisis técnico profesional bajo el perfil "{profile.name}".

---

### 📋 INSTRUCCIONES DE ANÁLISIS (REGLAS OBLIGATORIAS)

Realiza el análisis respetando estrictamente los siguientes principios:

#### 1. Análisis Arquitectónico y Dependencias
1. **Analiza la arquitectura del proyecto primero** antes de proponer cualquier cambio.
2. **Analiza las dependencias entre archivos**: cómo interactúan clases, funciones, componentes e importaciones.
3. **No asumas que un archivo funciona de forma aislada**: evalúa el impacto en otros componentes.

#### 2. Causa Raíz y Solución Escalable
4. **Identifica la causa raíz o el diseño adecuado**: no apliques parches temporales ni soluciones superficiales.
5. **Evita soluciones temporales**: propón soluciones escalables, limpias y mantenibles.
6. **Preserva la funcionalidad existente**: no elimines funcionalidades ni cambies comportamientos sin justificación técnica explícita.

#### 3. Especificidad de las Modificaciones
7. **Especifica exactamente qué archivos deben modificarse**, incluyendo la ruta relativa.
8. **Indica el número de línea aproximado** para cada modificación.
9. **Explica cada modificación** con su justificación técnica concisa.
10. **Muestra el código corregido/implementado** listo para copiar y pegar sin placeholders incompletos.
11. **Detecta posibles efectos secundarios** de cada cambio propuesto.
12. **Indica si se deben crear nuevos archivos** (con ruta y propósito).
13. **Indica si la estructura del proyecto debe modificarse**.

---

### 📐 FORMATO DE RESPUESTA OBLIGATORIO PARA: {profile.name.upper()}

Tu respuesta DEBE seguir **exactamente** la siguiente estructura Markdown adaptada al perfil seleccionado. No respondas con JSON. Esta respuesta la leerá un desarrollador directamente desde el chat web.

---

{profile.response_template}

---

==============================================================
ATTACHMENTS / ARCHIVOS ADJUNTOS
==============================================================
Por favor revisa el archivo de contexto adjunto (`deepseek_project_context.md` / `deepseek_project_context.txt`) que contiene:
- **Project Summary**: desglose de archivos seleccionados por extensión y total de líneas.
- **Dependencies and References**: importaciones y dependencias detectadas automáticamente por archivo.
- **Estructura del Proyecto**: diagrama en árbol jerárquico de carpetas y archivos.
- **Código Fuente**: contenido de los archivos seleccionados con sus **rutas relativas** y **números de línea originales** (`LINE X | ...`).

Confirma la recepción del contexto y responde siguiendo **exactamente** el formato estructurado indicado arriba para el perfil "{profile.name}".
"""
    return prompt
