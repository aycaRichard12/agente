# PROMPT PROFESIONAL PARA DEEPSEEK WEB CHAT

> **Instrucción para el usuario:** Copia este texto y pégalo directamente en el chat de DeepSeek junto con los archivos adjuntos (`deepseek_project_context.md` o `deepseek_project_context.txt`).

==============================================================
TIPO DE ANÁLISIS SELECCIONADO / SELECTED ANALYSIS PROFILE: 🔧 Solve problem
==============================================================
• OBJETIVO: Diagnosticar la causa raíz y resolver quirúrgicamente el problema específico reportado por el desarrollador.
• ENFOQUE: Solución directa, eficaz y de mínimo impacto colateral para la incidencia descrita.
• PRIORIDADES: 1. Causa raíz del síntoma reportado. 2. Corrección quirúrgica y mantenible. 3. Preservación estricta de la funcionalidad adyacente.
• RESULTADO ESPERADO: Diagnóstico directo, archivos exactos a modificar con líneas aproximadas, código de sustitución listo y plan de implementación paso a paso.

⚠️ REGLA DE CONCRECIÓN TÉCNICA Y ACCIÓN:
El análisis debe ser CONCRETO, TÉCNICO y ORIENTADO A LA ACCIÓN. Enfócate exclusivamente en resolver el problema reportado de raíz, sin desviarte a refactorizaciones no solicitadas.

==============================================================
REPORTED PROBLEM OR GOAL / PROBLEMA REPORTADO U OBJETIVO
==============================================================
Tengo el siguiente problema en el proyecto: [Describe aquí el error exacto, mensaje de excepción o comportamiento inesperado que deseas resolver].

==============================================================
PROJECT CONTEXT / CONTEXTO E INSTRUCCIONES DEL PROYECTO
==============================================================
Hola DeepSeek. Te adjunto el contexto completo de mi proyecto de software para su análisis técnico profesional bajo el perfil "Solve problem".

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

### 📐 FORMATO DE RESPUESTA OBLIGATORIO PARA: SOLVE PROBLEM

Tu respuesta DEBE seguir **exactamente** la siguiente estructura Markdown adaptada al perfil seleccionado. No respondas con JSON. Esta respuesta la leerá un desarrollador directamente desde el chat web.

---

# DIAGNOSIS
## Problem
[Descripción técnica del problema reportado]
## Root Cause
[Causa raíz exacta en el código]

# FILES TO MODIFY
## 1. [ruta/relativa/archivo.ext]
Approximate line: [número]
### Problem
[Problema en este archivo]
### Solution
[Solución aplicada]
### Current Code
```
[código actual]
```
### Corrected Code
```
[código corregido]
```

# NEW FILES
[Nuevos archivos requeridos o: No se requieren nuevos archivos.]

# RISKS OR SIDE EFFECTS
[Riesgos identificados o: Sin riesgos identificados.]

# IMPLEMENTATION PLAN
1. [Paso 1]
2. [Paso 2]

---

==============================================================
ATTACHMENTS / ARCHIVOS ADJUNTOS
==============================================================
Por favor revisa el archivo de contexto adjunto (`deepseek_project_context.md` / `deepseek_project_context.txt`) que contiene:
- **Project Summary**: desglose de archivos seleccionados por extensión y total de líneas.
- **Dependencies and References**: importaciones y dependencias detectadas automáticamente por archivo.
- **Estructura del Proyecto**: diagrama en árbol jerárquico de carpetas y archivos.
- **Código Fuente**: contenido de los archivos seleccionados con sus **rutas relativas** y **números de línea originales** (`LINE X | ...`).

Confirma la recepción del contexto y responde siguiendo **exactamente** el formato estructurado indicado arriba para el perfil "Solve problem".
