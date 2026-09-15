# PROMPT PROFESIONAL PARA DEEPSEEK WEB CHAT

> **Instrucción para el usuario:** Copia este texto y pégalo directamente en el chat de DeepSeek junto con los archivos adjuntos (`deepseek_project_context.md` o `deepseek_project_context.txt`).

==============================================================
MODO Y PERFIL DE ANÁLISIS SELECCIONADO
==============================================================
• MODO: 🔧 Modo Problema (Problem Mode)
• PERFIL: 🐞 Detect errors
• OBJETIVO: Identificar errores de sintaxis, bugs lógicos, excepciones no controladas, condiciones de carrera y fallos de tipo en el código.
• ENFOQUE: Detección exhaustiva de bugs, casos límite (edge cases), seguridad de nulos/undefined, control de flujo y manejo robusto de excepciones.
• PRIORIDADES: 1. Crashes y errores que detienen la ejecución. 2. Fallos silenciosos y corrupción de estado. 3. Manejo deficiente de excepciones. 4. Regresiones potenciales.
• RESULTADO ESPERADO: Localización exacta de cada error (archivo y línea), causa raíz técnica, código corregido listo para copiar/pegar y caso de prueba de verificación.

⚠️ REGLA DE CONCRECIÓN TÉCNICA Y ACCIÓN:
El análisis debe ser CONCRETO, TÉCNICO y ORIENTADO A LA ACCIÓN. Concéntrate exclusivamente en fallos reproducibles y errores verificables. Omite comentarios estilísticos o divagaciones teóricas que no resuelvan un error.

==============================================================
REPORTED PROBLEM / PROBLEMA REPORTADO
==============================================================
Por favor audita y detecta todos los errores, excepciones no controladas, fallos lógicos o condiciones de carrera presentes en el código adjunto.

==============================================================
PROJECT CONTEXT / CONTEXTO E INSTRUCCIONES DEL PROYECTO
==============================================================
Hola DeepSeek. Te adjunto el contexto completo de mi proyecto de software para su análisis técnico profesional bajo el modo "Modo Problema (Problem Mode)".

---

### 📋 INSTRUCCIONES DE ANÁLISIS (PROBLEM MODE RULES)

### 🎯 ENFOQUE DE MODO PROBLEMA (PROBLEM MODE)
1. **Foco exclusivo en el problema especificado**: Diagnostica y resuelve directamente la incidencia descrita en "REPORTED PROBLEM".
2. **Prioriza la Causa Raíz**: Identifica el origen exacto del fallo técnico antes de proponer cambios de código.
3. **Solución quirúrgica y escalable**: Genera el código corregido listo para sustituir sin alterar funcionalidades no relacionadas.
4. **Impacto y Efectos Secundarios**: Evalúa regresiones potenciales de la modificación realizada.

---

### 📐 FORMATO DE RESPUESTA OBLIGATORIO PARA: MODO PROBLEMA (PROBLEM MODE)

Tu respuesta DEBE seguir **exactamente** la siguiente estructura Markdown adaptada al modo seleccionado. No respondas con JSON. Esta respuesta la leerá un desarrollador directamente desde el chat web.

---

# DIAGNOSIS
## Detected Bugs
[Lista técnica de los bugs encontrados con su causa raíz exacta]

# FILES TO MODIFY
## 1. [ruta/relativa/archivo.ext]
Approximate line: [número]
### Bug Description
[Explicación concisa del error]
### Current Code
```
[código con error]
```
### Bugfix Code
```
[código corregido listo para sustituir]
```

# VERIFICATION & EDGE CASES
[Prueba o caso límite para verificar que el bug fue resuelto]

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
