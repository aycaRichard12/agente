# PROMPT PROFESIONAL PARA DEEPSEEK WEB CHAT

> **Instrucción para el usuario:** Copia este texto y pégalo directamente en el chat de DeepSeek junto con los archivos adjuntos (`deepseek_project_context.md` o `deepseek_project_context.txt`).

==============================================================
REPORTED PROBLEM / PROBLEMA REPORTADO
==============================================================
agregar mejoras a este proyecto para que sea mas provechoso

==============================================================
PROJECT CONTEXT / CONTEXTO E INSTRUCCIONES DEL PROYECTO
==============================================================
Hola DeepSeek. Te adjunto el contexto completo de mi proyecto de software para su análisis técnico profesional.

---

### 📋 INSTRUCCIONES DE ANÁLISIS (REGLAS OBLIGATORIAS)

Realiza un análisis exhaustivo respetando estrictamente los siguientes principios:

#### 1. Análisis Arquitectónico y Dependencias
1. **Analiza la arquitectura del proyecto primero** antes de proponer cualquier cambio.
2. **Analiza las dependencias entre archivos**: cómo interactúan clases, funciones, componentes e importaciones.
3. **No asumas que un archivo funciona de forma aislada**: evalúa el impacto en otros componentes.

#### 2. Causa Raíz y Solución Escalable
4. **Identifica la causa raíz del problema**: no apliques parches temporales ni soluciones superficiales.
5. **Evita soluciones temporales**: propón soluciones escalables, limpias y mantenibles.
6. **Preserva la funcionalidad existente**: no elimines funcionalidades ni cambies comportamientos sin justificación técnica explícita.

#### 3. Especificidad de las Modificaciones
7. **Especifica exactamente qué archivos deben modificarse**, incluyendo la ruta relativa.
8. **Indica el número de línea aproximado** para cada modificación.
9. **Explica cada modificación** con su justificación técnica.
10. **Muestra el código corregido** listo para copiar y pegar.
11. **Detecta posibles efectos secundarios** de cada cambio propuesto.
12. **Indica si se deben crear nuevos archivos** (con ruta y propósito).
13. **Indica si la estructura del proyecto debe modificarse**.

---

### 📐 FORMATO DE RESPUESTA OBLIGATORIO

Tu respuesta DEBE seguir **exactamente** la siguiente estructura Markdown. No respondas con JSON. Esta respuesta la leerá un desarrollador directamente desde el chat web.

---

# DIAGNOSIS

## Problem
[Descripción clara y técnica del problema detectado en el código]

## Root Cause
[Explicación técnica de la causa raíz. ¿Por qué ocurre? ¿Qué lo genera?]

---

# FILES TO MODIFY

## 1. [ruta/relativa/archivo.ext]
Approximate line: [número aproximado de línea]

### Problem
[Descripción precisa del problema en este archivo]

### Solution
[Descripción detallada de la modificación propuesta]

### Current Code
```
[bloque de código actual que debe reemplazarse]
```

### Corrected Code
```
[bloque de código corregido listo para sustituir]
```

---
[Repite la sección anterior para cada archivo que deba modificarse]

---

# NEW FILES
[Si se requieren nuevos archivos, lístallos aquí con su ruta relativa, propósito y contenido de ejemplo.
Si no se requieren nuevos archivos, escribe: No se requieren nuevos archivos.]

---

# ARCHITECTURAL CHANGES
[Describe si la estructura de carpetas, módulos o dependencias del proyecto debe modificarse.
Si no se requieren cambios arquitectónicos, escribe: No se requieren cambios arquitectónicos.]

---

# RISKS OR SIDE EFFECTS
[Lista de posibles riesgos, efectos secundarios o regresiones que podrían ocurrir al aplicar los cambios propuestos.
Si no hay riesgos identificados, escribe: Sin riesgos identificados.]

---

# IMPLEMENTATION PLAN
[Lista ordenada y numerada de pasos concretos para implementar los cambios de forma segura:]

1. [Primer paso]
2. [Segundo paso]
3. [Tercer paso]
4. [Cuarto paso]
[...continúa según sea necesario]

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
