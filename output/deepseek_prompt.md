# PROMPT PROFESIONAL PARA DEEPSEEK WEB CHAT

> **Instrucción para el usuario:** Copia este texto y pégalo directamente en el chat de DeepSeek junto con los archivos adjuntos (`deepseek_project_context.md` o `deepseek_project_context.txt`).

==============================================================
REPORTED PROBLEM / PROBLEMA REPORTADO
==============================================================
The `CotizacionPage.vue` file is being optimized and refactored to create a modular, scalable, and easily maintainable structure.

Analyze the current code of `CotizacionPage.vue` in detail and compare it to the modular implementation located in:

`modules/cotizacion`

The goal is to identify **why the optimized/modular version is not working correctly**, while maintaining the exact same functionality and behavior as `CotizacionPage.vue`.

Perform the analysis following these rules:

1. First, analyze `CotizacionPage.vue` to understand:

* All its functionalities.

* Data flow.

* Reactive states.

* Props and emits.

* Methods and functions.

* API calls.

* Events.

* Dependencies between components.

* Stores, composables, and utilities used.

* Validation logic and calculations.

* Interface behaviors.

2. Next, analyze the entire `modules/cotizacion` structure and determine:

* Which functionalities were correctly ported.

* Which functionalities are missing.

* Which logic was incorrectly modified.

* Which imports, exports, or references are incorrect.

* Composition API issues, reactivity, props, emits, or events.

* Routing or module resolution issues.

* Pinia, composable, or service issues.

* Variable or function naming issues.

* Circular dependencies or incorrect coupling.

* Errors that could cause the module to malfunction.

* Behavioral differences between the original and modular versions.

3. Do not assume that the modular architecture is correctly implemented. Verify each part against the original functionality of `CotizacionPage.vue`.

4. Identify exactly where each problem is located, indicating:

* File.

* Approximate or exact line number.

* Problematic code.

* Cause of the problem.

* Proposed fix.

5. If there are related errors across multiple files, clearly explain the dependency chain that causes the failure.

6. The refactoring must preserve **100% of the existing functionality** of `CotizacionPage.vue`. Do not remove functionality or change functional behavior without justification.

7. The solution must maintain an architecture that is:

* Modular.

* Scalable.

* Maintainable.

* With clearly separated responsibilities.

* Avoiding excessively large files.

* Avoiding code duplication.

* With reusable components and composables where appropriate.

8. If you find an incorrect modular implementation, correct it by referencing the functional logic of `CotizacionPage.vue`, but without recreating a monolithic file.

9. Before proposing changes, provide a clear diagnosis of why `modules/cotizacion` is currently not working.

10. After the diagnosis, provide the necessary modifications file by file, indicating exactly what needs to be changed.

11. Finally, conceptually verify that the corrected version of `modules/cotizacion` retains all the functionalities of `CotizacionPage.vue`.

### Required Response Format

Organize your response as follows:

**1. General Diagnosis**

* Main cause of the problem.

* Other problems encountered.

**2. Functional Comparison**

* Functionalities of `CotizacionPage.vue`.

* Status of each functionality in `modules/cotizacion`: correct, incomplete, or incorrect.

**3. Errors Found**
For each error:

* File.

* Line.

* Problem.

* Cause.

* Solution.

**4. Corrections**
Specify the specific changes that need to be made to each file.

**5. Final Architecture**
Show how the `modules/cotizacion` structure should look to ensure scalability.

**6. Final Verification**
Confirm that all the original functionalities of `CotizacionPage.vue` are covered by the new architecture.

Do not make changes based on assumptions. If a functionality or dependency cannot be determined with certainty from the provided files, state this explicitly.

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
