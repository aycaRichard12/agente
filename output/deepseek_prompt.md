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
## 1. OBJETIVO PRINCIPAL
Analiza el proyecto completo adjunto y **implementa el cambio solicitado directamente sobre la arquitectura existente**.

No te limites a describir una posible solución.

Debes:

1. Comprender primero la arquitectura actual.
2. Identificar los módulos, clases, funciones y componentes relacionados con el requerimiento.
3. Seguir las referencias entre archivos para determinar el impacto real del cambio.
4. Detectar si el contexto proporcionado es suficiente.
5. Si falta contexto necesario para implementar correctamente el cambio, **identificar explícitamente qué archivo, función, clase, dependencia o información falta y continuar el análisis utilizando toda la información disponible**.
6. Determinar todos los archivos que deben modificarse.
7. Determinar si es necesario crear nuevos archivos.
8. Mantener la arquitectura, patrones y convenciones existentes del proyecto.
9. Evitar duplicar funcionalidad que ya exista.
10. Implementar una solución completa y coherente, no solamente un parche parcial.
11. Verificar que el cambio no rompa funcionalidades existentes.
12. Proponer y/o agregar pruebas para validar el comportamiento implementado.

---

# 2. REQUERIMIENTO FUNCIONAL

### Problema / Cambio solicitado

Quiero agregar un **buscador de archivos** al proyecto.

Además, cada archivo mostrado en el buscador debe tener una acción/botón que permita analizar sus dependencias.

Cuando el usuario presione ese botón:

1. Debe identificarse el archivo seleccionado como nodo raíz.
2. Debe analizarse qué archivos, módulos o componentes utiliza/importa ese archivo.
3. Cada dependencia encontrada debe convertirse en un nuevo nodo del árbol.
4. Para cada dependencia encontrada se debe volver a analizar qué otros archivos utiliza.
5. El proceso debe continuar recursivamente hasta construir el árbol completo de dependencias disponibles dentro del proyecto.
6. El usuario debe poder visualizar claramente la relación:

```text
Archivo seleccionado
├── Dependencia A
│   ├── Dependencia A.1
│   ├── Dependencia A.2
│   └── Dependencia A.3
├── Dependencia B
│   ├── Dependencia B.1
│   └── Dependencia B.2
└── Dependencia C
    └── Dependencia C.1
```

7. El usuario debe poder seleccionar:

   * solamente el archivo raíz;
   * una dependencia individual;
   * una rama completa;
   * todas las dependencias encontradas;
   * o todos los archivos del árbol mediante una acción tipo **"Seleccionar todos"**.

8. La selección realizada debe integrarse con el sistema de selección de archivos existente.

9. Si un archivo ya está seleccionado, debe evitarse duplicarlo.

10. Si existen dependencias circulares, el sistema debe detectarlas y evitar ciclos infinitos.

Ejemplo:

```text
A.py
└── B.py
    └── C.py
        └── A.py   ← dependencia circular
```

El árbol debe detectar esta situación y mostrarla correctamente sin entrar en recursión infinita.

---

# 3. ANÁLISIS OBLIGATORIO ANTES DE MODIFICAR

Antes de proponer código, analiza obligatoriamente:

### Arquitectura

Identifica:

* interfaz gráfica;
* gestión de selección de archivos;
* escaneo del proyecto;
* lectura de archivos;
* detección de dependencias;
* modelos de datos;
* generación de contexto;
* generación de prompts;
* componentes reutilizables relacionados con árboles;
* pruebas existentes.

### Componentes especialmente relevantes

Revisa como mínimo los componentes relacionados con:

```text
app/core/dependency_detector.py
app/core/file_selector.py
app/core/project_scanner.py
app/core/project_structure.py
app/core/intelligent_context.py
app/gui/file_tree.py
app/gui/main_window.py
app/models/project.py
```

También debes revisar cualquier otro archivo que las referencias del proyecto indiquen como necesario.

**No asumas que la lista anterior es completa.**

Si durante el análisis encuentras otro archivo que participa en el flujo, debes incluirlo.

---

# 4. REGLA DE DESCUBRIMIENTO DE CONTEXTO

Esta regla es obligatoria.

El contexto proporcionado contiene una selección de archivos del proyecto, pero puede no contener todos los archivos necesarios para implementar el cambio.

Por lo tanto:

### NO debes asumir:

* que los archivos proporcionados son suficientes;
* que una función no existe simplemente porque no aparece en el contexto;
* que una dependencia no existe;
* que un componente debe crearse cuando posiblemente ya existe uno reutilizable.

### Debes identificar:

* archivos faltantes;
* funciones faltantes;
* clases faltantes;
* módulos relacionados;
* dependencias no resueltas;
* referencias cuyo destino no está incluido;
* información necesaria para completar correctamente la implementación.

Cuando falte contexto:

```text
CONTEXTO FALTANTE DETECTADO
├── Archivo:
├── Función / clase:
├── Motivo por el que es necesario:
├── Relación con el cambio:
└── Acción recomendada:
```

No inventes el contenido del archivo faltante.

Si no puedes verificar una implementación debido a contexto insuficiente, debes indicarlo claramente.

---

# 5. REGLA DE ANÁLISIS DE DEPENDENCIAS

No analices las dependencias únicamente mediante coincidencias de nombres.

Debes utilizar, en la medida que el código existente lo permita:

* imports;
* requires;
* includes;
* referencias entre módulos;
* rutas relativas;
* rutas absolutas;
* nombres de módulos;
* paquetes;
* componentes;
* clases;
* funciones;
* referencias internas;
* configuración del proyecto.

La dependencia debe resolverse contra archivos reales del proyecto cuando sea posible.

Ejemplo:

```python
from app.core.file_selector import FileSelectorManager
```

No basta con mostrar:

```text
app.core.file_selector
```

Debe intentarse resolver:

```text
app/core/file_selector.py
```

como archivo real del proyecto.

---

# 6. ÁRBOL DE DEPENDENCIAS

La implementación debe considerar un grafo de dependencias y no únicamente una lista plana.

Conceptualmente:

```text
RootFile
   ↓
DependencyResolver
   ↓
DependencyGraph
   ↓
TreeView
```

El sistema debe mantener información equivalente a:

```text
source_file
dependency_file
relationship
depth
visited
```

Debe existir protección contra:

* ciclos;
* dependencias repetidas;
* archivos inexistentes;
* imports externos;
* módulos estándar;
* dependencias que no puedan resolverse;
* rutas inválidas;
* archivos excluidos;
* archivos binarios;
* errores de lectura.

Las dependencias externas que no correspondan a archivos del proyecto **no deben aparecer como si fueran archivos internos**.

Si es útil mostrarlas, deben distinguirse claramente como dependencias externas.

---

# 7. INTEGRACIÓN CON LA GUI EXISTENTE

No construyas una segunda lógica de selección independiente si el proyecto ya posee un sistema de selección.

Analiza primero el componente existente.

La nueva funcionalidad debe integrarse con:

```text
FileSelectorManager
ProjectSelection
CheckboxTreeview
MainWindow
```

o con los componentes equivalentes encontrados durante el análisis.

La selección realizada desde el árbol de dependencias debe terminar utilizando el mismo estado de selección del proyecto.

Debe mantenerse la coherencia entre:

```text
Árbol principal de archivos
        ↕
Árbol de dependencias
        ↕
ProjectSelection
        ↕
Generación del contexto
```

---

# 8. COMPORTAMIENTO DE SELECCIÓN

Implementa como mínimo:

### Seleccionar archivo

Selecciona únicamente el nodo actual.

### Seleccionar rama

Selecciona el nodo y todos sus descendientes.

### Seleccionar todos

Selecciona todos los nodos resolubles del árbol.

### Deseleccionar rama

Deselecciona el nodo y todos sus descendientes.

### Evitar duplicados

Si un archivo ya forma parte de:

```text
checked_folder_files
```

o:

```text
individual_files
```

no debe agregarse nuevamente.

### Estado visual

El usuario debe poder distinguir claramente:

```text
☐ No seleccionado
☑ Seleccionado
▣ Parcialmente seleccionado
```

si la implementación del componente lo permite.

---

# 9. RENDIMIENTO

La solución debe evitar analizar repetidamente el mismo archivo.

Utiliza mecanismos apropiados de caché o conjuntos de visitados.

Por ejemplo:

```text
visited_files
dependency_cache
```

No debes ejecutar recursivamente un análisis completo del mismo archivo cada vez que aparezca como dependencia.

Debe considerarse el comportamiento con proyectos grandes.

---

# 10. COMPATIBILIDAD

La solución debe respetar:

* Python y versión utilizada actualmente por el proyecto;
* Tkinter/ttk existente;
* arquitectura modular;
* imports existentes;
* convenciones de nombres;
* sistema actual de selección;
* sistema de generación de contexto;
* exclusiones configuradas;
* tests existentes.

No introduzcas dependencias externas nuevas si la funcionalidad puede implementarse utilizando la arquitectura y librerías existentes.

Si una nueva dependencia externa fuera realmente necesaria, debes justificarla antes de utilizarla.

---

# 11. ARCHIVOS A MODIFICAR

Determina primero el impacto.

Devuelve una lista como:

```text
FILES TO CREATE
1. ...
2. ...

FILES TO MODIFY
1. ...
2. ...

FILES TO TEST
1. ...
2. ...
```

Para cada archivo explica:

* por qué debe modificarse;
* qué responsabilidad tendrá después del cambio;
* qué componente existente reutiliza;
* qué impacto tiene sobre el resto del sistema.

---

# 12. IMPLEMENTACIÓN

La solución debe ser código real y coherente con el código existente.

No utilices pseudocódigo cuando puedas proporcionar implementación real.

Para cada archivo modificado proporciona:

```text
Archivo:
Ruta:

Cambio:
...

Motivo:
...

Código:
```

Cuando sea posible, proporciona el bloque completo de la función/clase modificada listo para reemplazar.

No reemplaces innecesariamente archivos completos si solamente es necesario modificar una función.

---

# 13. PRUEBAS

Debes crear o modificar pruebas para cubrir como mínimo:

### Caso 1

Archivo sin dependencias.

### Caso 2

Archivo con una dependencia.

### Caso 3

Cadena de dependencias:

```text
A → B → C → D
```

### Caso 4

Dependencia circular:

```text
A → B → C → A
```

### Caso 5

Dependencia repetida:

```text
A → B
A → C
B → D
C → D
```

`D` no debe procesarse dos veces.

### Caso 6

Dependencia externa.

### Caso 7

Archivo inexistente.

### Caso 8

Selección de toda la rama.

### Caso 9

Selección de todos los nodos.

### Caso 10

Archivo que ya estaba seleccionado.

### Caso 11

Proyecto grande.

### Caso 12

Compatibilidad con el flujo actual de generación de contexto.

---

# 14. VALIDACIÓN FINAL

Antes de considerar terminada la implementación, verifica:

* ¿El buscador encuentra los archivos correctamente?
* ¿Cada archivo puede iniciar un análisis de dependencias?
* ¿El árbol se construye correctamente?
* ¿Las dependencias se resuelven contra archivos reales?
* ¿Se detectan ciclos?
* ¿Se evitan duplicados?
* ¿Se puede seleccionar una rama?
* ¿Se puede seleccionar todo?
* ¿La selección se sincroniza con el sistema existente?
* ¿Se mantienen las exclusiones?
* ¿Se manejan errores de lectura?
* ¿Se manejan archivos inexistentes?
* ¿Se manejan dependencias externas?
* ¿Se evita repetir análisis?
* ¿Las pruebas cubren los casos críticos?
* ¿El cambio rompe alguna funcionalidad existente?

---

# 15. REGLA CRÍTICA

**NO IMPLEMENTES UNA SOLUCIÓN PARCIAL.**

Si para cumplir correctamente el requerimiento es necesario modificar varios componentes, modifica todos los componentes necesarios.

Si el contexto actual no contiene información suficiente para garantizar una implementación correcta:

1. identifica exactamente qué falta;
2. no inventes código inexistente;
3. determina qué archivos adicionales deberían incluirse;
4. explica por qué son necesarios;
5. utiliza toda la información disponible para completar el resto del análisis.

---

# 16. FORMATO OBLIGATORIO DE RESPUESTA

La respuesta debe tener exactamente estas secciones:

# 1. UNDERSTANDING

Explica brevemente qué entendiste del requerimiento.

# 2. CURRENT ARCHITECTURE

Explica qué componentes actuales participan y cómo se relacionan.

# 3. IMPACT ANALYSIS

Explica qué partes del proyecto deben cambiar.

# 4. MISSING CONTEXT

Si falta contexto:

```text
Archivo:
Motivo:
Información necesaria:
Impacto:
```

Si no falta:

```text
No se detectó contexto crítico faltante.
```

# 5. IMPLEMENTATION PLAN

Lista ordenada de cambios.

# 6. FILES TO CREATE

Lista de archivos nuevos.

# 7. FILES TO MODIFY

Lista de archivos existentes que deben modificarse.

# 8. CODE CHANGES

Código concreto listo para implementar.

# 9. TESTS

Pruebas nuevas o modificadas.

# 10. EDGE CASES

Casos límite considerados.

# 11. VALIDATION

Verificación final de que el requerimiento completo fue cubierto.

# 12. FINAL IMPLEMENTATION SUMMARY

Resumen técnico de los cambios realizados.

---

## REGLAS ABSOLUTAS

* No inventar archivos.
* No inventar funciones.
* No asumir arquitectura que no esté respaldada por el código.
* No ignorar archivos relacionados.
* No modificar componentes sin justificarlo.
* No duplicar lógica existente.
* No crear una arquitectura paralela innecesaria.
* No entregar únicamente teoría.
* No entregar únicamente pseudocódigo.
* No limitarse al primer archivo que parezca relacionado.
* Seguir las dependencias hasta comprender el flujo completo.
* Mantener compatibilidad con el código existente.
* Priorizar reutilización de componentes existentes.
* Detectar contexto faltante antes de implementar.
* Señalar explícitamente cualquier incertidumbre.
* No afirmar que algo fue implementado si solamente fue propuesto.
* No responder con JSON.
* Responder en Markdown.
* El código debe estar listo para copiar, adaptar e implementar.

**Objetivo final: entregar una solución completa, integrada y verificable, no solamente una recomendación.**
quiero agregar un buscardo de archivos 
agerar un boton  para cada archivo y al precionar me arme el arbol de que archivos esta utilizando,  ejemplo cotizacion y despues de precionar poder ver como un arbol que archivos importa y esos importados que otros componentes utiliza hasta armar el arbol completo y poder seleccionar todos

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
