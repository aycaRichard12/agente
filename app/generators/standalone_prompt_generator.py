"""Generates standalone professional prompt deepseek_prompt.md with structured DeepSeek response template."""
from app.models.analysis_types import get_analysis_profile
from app.models.analysis_modes import get_analysis_mode_config, MODE_PROJECT, MODE_PROBLEM


def generate_standalone_prompt(
    problem_desc: str = "",
    analysis_type: str = "Detect errors",
    analysis_mode: str = "problem"
) -> str:
    """
    Generates a professional copy-paste prompt instructing DeepSeek:
    - Problem Mode: Focuses exclusively on diagnosing & resolving the specified problem (root cause, solution, code changes).
    - Project Mode: Audits the project holistically (errors, duplicate code, bad practices, architecture, security, performance).
    """
    profile = get_analysis_profile(analysis_type)
    mode_cfg = get_analysis_mode_config(analysis_mode)
    is_project_mode = (mode_cfg.mode == MODE_PROJECT)

    if is_project_mode:
        problem_block = """==============================================================
SCOPE OF ANALYSIS / ALCANCE DE AUDITORÍA HOLÍSTICA (MODO PROYECTO)
==============================================================
Realiza una auditoría técnica transversal completa de todo el proyecto adjunto:
• Detección de errores y bugs latentes en el código.
• Identificación de código duplicado y deuda técnica (DRY).
• Malas prácticas de programación e ineficiencias.
• Deficiencias de arquitectura, acoplamiento indebido y separación de capas.
• Vulnerabilidades de seguridad (OWASP) y riesgos de exposición.
• Oportunidades concretas de optimización de rendimiento (CPU, memoria, I/O)."""
        response_template_to_use = mode_cfg.response_template
    else:
        problem_text = problem_desc.strip() if problem_desc.strip() else "[Describe aquí el problema o incidencia que deseas resolver]"
        problem_block = f"""==============================================================
REPORTED PROBLEM / PROBLEMA REPORTADO
==============================================================
{problem_text}"""
        response_template_to_use = profile.response_template

    prompt = f"""# PROMPT PROFESIONAL PARA DEEPSEEK WEB CHAT

> **Instrucción para el usuario:** Copia este texto y pégalo directamente en el chat de DeepSeek junto con los archivos adjuntos (`deepseek_project_context.md` o `deepseek_project_context.txt`).

==============================================================
MODO Y PERFIL DE ANÁLISIS SELECCIONADO
==============================================================
• MODO: {mode_cfg.icon} {mode_cfg.display_name}
• PERFIL: {profile.icon} {profile.name}
• OBJETIVO: {profile.objective if not is_project_mode else mode_cfg.description}
• ENFOQUE: {profile.focus}
• PRIORIDADES: {profile.priorities}
• RESULTADO ESPERADO: {profile.expected_outcome}

⚠️ REGLA DE CONCRECIÓN TÉCNICA Y ACCIÓN:
{profile.response_instructions}

{problem_block}

==============================================================
PROJECT CONTEXT / CONTEXTO E INSTRUCCIONES DEL PROYECTO
==============================================================
Hola DeepSeek. Te adjunto el contexto completo de mi proyecto de software para su análisis técnico profesional bajo el modo "{mode_cfg.display_name}".

---

### 📋 INSTRUCCIONES DE ANÁLISIS ({mode_cfg.mode.upper()} MODE RULES)

{mode_cfg.prompt_instructions}

---

### 📐 FORMATO DE RESPUESTA OBLIGATORIO PARA: {mode_cfg.display_name.upper()}

Tu respuesta DEBE seguir **exactamente** la siguiente estructura Markdown adaptada al modo seleccionado. No respondas con JSON. Esta respuesta la leerá un desarrollador directamente desde el chat web.

---

{response_template_to_use}

---

==============================================================
ATTACHMENTS / ARCHIVOS ADJUNTOS
==============================================================
Por favor revisa el archivo de contexto adjunto (`deepseek_project_context.md` / `deepseek_project_context.txt`) que contiene:
- **Project Summary**: desglose de archivos seleccionados por extensión y total de líneas.
- **Dependencies and References**: importaciones y dependencias detectadas automáticamente por archivo.
- **Estructura del Proyecto**: diagrama en árbol jerárquico de carpetas y archivos.
- **Código Fuente**: contenido de los archivos seleccionados con sus **rutas relativas** y **números de línea originales** (`LINE X | ...`).

Confirma la recepción del contexto y responde siguiendo **exactamente** el formato estructurado indicado arriba.
"""
    return prompt
