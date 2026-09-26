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
## OBJETIVO

Genera un **script Python ejecutable** que aplique automáticamente los cambios correspondientes a esta fase sobre el proyecto existente.

El script debe modificar únicamente los archivos necesarios y preservar intacta la lógica no relacionada.

## REQUISITOS DEL SCRIPT

1. **Detectar automáticamente la raíz del proyecto** a partir de la ubicación desde donde se ejecuta o recibirla como argumento:

```bash
python3 aplicar_cambios.py /ruta/al/proyecto
```

2. Antes de modificar cualquier archivo:

   * Verificar que los archivos objetivo existan.
   * Validar que el contenido esperado esté presente.
   * Si la estructura esperada no coincide, detenerse y mostrar un error claro.
   * **No sobrescribir archivos de forma ciega.**

3. Crear automáticamente una copia de seguridad de cada archivo que será modificado:

```text
.backup/
```

La copia debe conservar la ruta relativa original.

4. Aplicar los cambios de forma **idempotente**:

   * Ejecutar el script una segunda vez no debe duplicar código.
   * Detectar si un cambio ya fue aplicado.
   * No insertar funciones, imports, tablas o bloques duplicados.

5. Mantener el código existente:

   * No eliminar lógica funcional.
   * No reformatear archivos completos innecesariamente.
   * No modificar código fuera del alcance de esta fase.
   * Preservar indentación y estilo existente.

6. Si es necesario crear archivos nuevos, generarlos con el contenido completo requerido.

7. Mostrar durante la ejecución:

```text
[INFO] Proyecto detectado: ...
[INFO] Archivo encontrado: ...
[INFO] Backup creado: ...
[INFO] Modificando: ...
[OK] Cambio aplicado: ...
[SKIP] Cambio ya aplicado: ...
[ERROR] ...
```

8. Al finalizar mostrar un resumen:

```text
Archivos modificados: X
Archivos creados: X
Archivos omitidos: X
Backups creados: X
Errores: X
```

9. Si ocurre cualquier error durante la modificación:

   * detener el proceso;
   * no continuar aplicando cambios;
   * informar exactamente qué archivo y operación fallaron.

10. El script debe utilizar únicamente la biblioteca estándar de Python siempre que sea posible.

## VALIDACIÓN FINAL

Después de aplicar los cambios:

* Verificar que los archivos modificados sigan siendo sintácticamente válidos.
* Para archivos `.py`, utilizar:

```bash
python3 -m py_compile archivo.py
```

* Informar cualquier error encontrado.

## IMPORTANTE

El script **no debe implementar funcionalidades adicionales** que no estén especificadas en esta fase.

Antes de generar el código del script:

1. Analiza la estructura real del proyecto.
2. Identifica exactamente qué archivos deben modificarse.
3. Determina los puntos concretos donde deben aplicarse los cambios.
4. Genera el script Python completo.
5. El script debe poder ejecutarse directamente desde terminal.

### ENTREGA

Entrega únicamente:

* el archivo/script Python completo;
* una explicación breve de cómo ejecutarlo;
* una lista breve de los archivos que modificará.

No generes pseudocódigo ni fragmentos incompletos.
generame el script python para hacer los cambios 
# FASE 1 — IMPLEMENTAR PERSISTENCIA SQLITE PARA NODOS

## OBJETIVO

Implementar la infraestructura de persistencia SQLite para almacenar la estructura de los proyectos analizados, sus métricas, dependencias y selección de nodos.

**En esta fase NO implementar todavía el Delta Scan ni la detección incremental de cambios.**

La aplicación debe continuar funcionando con el flujo actual de análisis.

---

## 1. CREAR `app/core/storage/database.py`

Crear un módulo responsable exclusivamente de:

* Crear y abrir la base SQLite.
* Inicializar las tablas.
* Ejecutar consultas y actualizaciones.
* Gestionar transacciones.
* Proporcionar operaciones CRUD necesarias para proyectos y nodos.

Ubicar `project_cache.db` en:

```text
.cache/project_cache.db
```

o, si la arquitectura actual ya dispone de una ruta global de datos de usuario, utilizar:

```text
~/.analyzer_app/project_cache.db
```

Reutilizar la estrategia de rutas existente del proyecto si ya existe.

---

## 2. ESQUEMA SQLITE

Crear las siguientes tablas:

```sql
CREATE TABLE IF NOT EXISTS projects (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    path TEXT UNIQUE NOT NULL,
    project_type TEXT,
    framework TEXT,
    last_scanned TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS nodes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    project_id INTEGER NOT NULL,
    rel_path TEXT NOT NULL,
    parent_path TEXT,
    is_dir BOOLEAN NOT NULL,
    mtime REAL NOT NULL,
    lines_count INTEGER DEFAULT 0,
    file_size INTEGER DEFAULT 0,
    is_important BOOLEAN DEFAULT 0,
    is_checked BOOLEAN DEFAULT 1,
    FOREIGN KEY(project_id) REFERENCES projects(id) ON DELETE CASCADE,
    UNIQUE(project_id, rel_path)
);

CREATE TABLE IF NOT EXISTS node_dependencies (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    source_node_id INTEGER NOT NULL,
    target_path TEXT NOT NULL,
    FOREIGN KEY(source_node_id) REFERENCES nodes(id) ON DELETE CASCADE
);

CREATE INDEX IF NOT EXISTS idx_nodes_rel_path
ON nodes(project_id, rel_path);

CREATE INDEX IF NOT EXISTS idx_nodes_parent
ON nodes(project_id, parent_path);
```

Activar:

```sql
PRAGMA foreign_keys = ON;
```

---

## 3. OPERACIONES NECESARIAS

Implementar métodos para:

* Obtener o crear un proyecto por ruta.
* Obtener todos los nodos de un proyecto.
* Insertar nodos en lote.
* Actualizar nodos.
* Eliminar nodos.
* Guardar dependencias.
* Obtener dependencias.
* Actualizar `is_checked`.
* Actualizar `last_scanned`.
* Eliminar completamente un proyecto de la caché.

Priorizar operaciones en lote mediante `executemany()` y transacciones.

---

## 4. INTEGRACIÓN INICIAL

Integrar `database.py` con el flujo actual de `ProjectAnalyzer` únicamente para:

1. Registrar el proyecto después de un análisis.
2. Guardar los nodos generados.
3. Guardar las métricas disponibles.
4. Guardar las dependencias detectadas.
5. Persistir `is_checked`.

El análisis actual debe seguir funcionando exactamente igual.

**No modificar la lógica de detección/análisis existente salvo lo estrictamente necesario para persistir los resultados.**

---

## 5. PERSISTENCIA DE CHECKBOX

Modificar `CheckboxTreeview` para persistir:

```text
is_checked
```

Cuando el usuario marque/desmarque un nodo:

* actualizar SQLite de forma diferida, o
* acumular cambios y guardarlos al finalizar/guardar el análisis.

Al volver a abrir el proyecto:

* recuperar `is_checked` desde SQLite;
* restaurar automáticamente la selección anterior.

---

## RESTRICCIONES

* No implementar Delta Scan todavía.
* No eliminar el análisis completo actual.
* No cambiar la API pública de `ProjectAnalyzer`.
* No cambiar la estructura de `FileMetric`.
* No modificar funcionalidades no relacionadas.
* Mantener compatibilidad con proyectos existentes.
* Evitar consultas SQLite individuales dentro de bucles cuando puedan hacerse en lote.

---

## VERIFICACIÓN

Comprobar que:

1. La base SQLite se crea correctamente.
2. Un proyecto analizado genera sus registros.
3. Los nodos y dependencias quedan almacenados.
4. `is_checked` se conserva después de cerrar y abrir la aplicación.
5. Reabrir un proyecto no produce errores.
6. El análisis actual sigue entregando los mismos resultados que antes.

Al finalizar, mostrar:

* archivos modificados;
* funciones nuevas;
* funciones modificadas;
* posibles problemas detectados.

**No comenzar la Fase 2 hasta que esta fase esté funcionando correctamente.**
que puedo hacer para mejorar la velocidad 
dame una lluvia de ideas

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
