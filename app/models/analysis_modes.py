"""
Analysis Modes definitions and directives.
Supports:
- MODE_PROBLEM ("problem"): Displays problem description field, focuses AI strictly on diagnosing & resolving the specified problem (root cause, solution, code changes).
- MODE_PROJECT ("project"): Hides problem field, performs a holistic project audit (errors, duplicate code, bad practices, architecture, security, performance) with prioritized findings & recommended actions.
"""
from dataclasses import dataclass
from typing import Dict

MODE_PROBLEM = "problem"
MODE_PROJECT = "project"


@dataclass
class AnalysisModeConfig:
    mode: str
    display_name: str
    icon: str
    description: str
    prompt_instructions: str
    response_template: str


ANALYSIS_MODES: Dict[str, AnalysisModeConfig] = {
    MODE_PROBLEM: AnalysisModeConfig(
        mode=MODE_PROBLEM,
        display_name="Modo Problema (Problem Mode)",
        icon="🔧",
        description="Enfoca a la IA exclusivamente en diagnosticar y resolver el problema específico reportado por el desarrollador, priorizando la causa raíz y las soluciones quirúrgicas en código.",
        prompt_instructions="""### 🎯 ENFOQUE DE MODO PROBLEMA (PROBLEM MODE)
1. **Foco exclusivo en el problema especificado**: Diagnostica y resuelve directamente la incidencia descrita en "REPORTED PROBLEM".
2. **Prioriza la Causa Raíz**: Identifica el origen exacto del fallo técnico antes de proponer cambios de código.
3. **Solución quirúrgica y escalable**: Genera el código corregido listo para sustituir sin alterar funcionalidades no relacionadas.
4. **Impacto y Efectos Secundarios**: Evalúa regresiones potenciales de la modificación realizada.""",
        response_template="""# DIAGNOSIS
## Reported Problem Summary
[Resumen del problema especificado]

## Root Cause
[Explicación técnica detallada de la causa raíz identificada]

# FILES TO MODIFY
## 1. [ruta/relativa/archivo.ext]
Approximate line: [número de línea]

### Problem in File
[Descripción técnica de la falla en este archivo]

### Solution & Justification
[Explicación concisa del arreglo]

### Current Code
```
[bloque de código actual]
```

### Corrected Code
```
[bloque de código corregido listo para copiar/pegar]
```

# NEW FILES
[Lista de nuevos archivos requeridos o: No se requieren nuevos archivos.]

# RISKS OR SIDE EFFECTS
[Efectos secundarios potenciales o: Sin riesgos identificados.]

# IMPLEMENTATION PLAN
1. [Paso 1 para aplicar la solución]
2. [Paso 2]"""
    ),

    MODE_PROJECT: AnalysisModeConfig(
        mode=MODE_PROJECT,
        display_name="Modo Proyecto (Project Mode)",
        icon="🏗️",
        description="Analiza el proyecto de forma holística: detecta errores latentes, código duplicado, malas prácticas, vulnerabilidades de seguridad, problemas arquitectónicos y oportunidades de optimización.",
        prompt_instructions="""### 🎯 ENFOQUE DE MODO PROYECTO (HOLISTIC PROJECT MODE)
1. **Análisis Holístico Transversal**: Evalúa la totalidad del proyecto analizando:
   - Errores sintácticos y de lógica latentes.
   - Código duplicado y deuda técnica (DRY).
   - Malas prácticas e ineficiencias de diseño.
   - Problemas arquitectónicos y acoplamiento indebido.
   - Vulnerabilidades de seguridad (OWASP).
   - Oportunidades de optimización de rendimiento.
2. **Matriz de Hallazgos Priorizada**: Clasifica cada problema encontrado por categoría y nivel de severidad (Crítica, Alta, Media, Baja).
3. **Acciones Recomendadas**: Proporciona el código de remediación directo y una hoja de ruta ordenada por impacto.""",
        response_template="""# HOLISTIC PROJECT AUDIT MATRIX
| Categoría | Severidad | Hallazgo Técnico | Ubicación (Archivo:Línea) |
|---|---|---|---|
| Errores / Bugs | [Crítica/Alta/Media/Baja] | [Descripción del error] | [Ruta:Línea] |
| Código Duplicado | [Crítica/Alta/Media/Baja] | [Fragmento duplicado o smell] | [Ruta:Línea] |
| Malas Prácticas | [Crítica/Alta/Media/Baja] | [Violación de estándar/convención] | [Ruta:Línea] |
| Arquitectura | [Crítica/Alta/Media/Baja] | [Acoplamiento / problema estructural] | [Ruta:Línea] |
| Seguridad | [Crítica/Alta/Media/Baja] | [Vulnerabilidad o riesgo] | [Ruta:Línea] |
| Rendimiento | [Crítica/Alta/Media/Baja] | [Iniciativa de optimización] | [Ruta:Línea] |

# PRIORITIZED REMEDIATION CODE
## 1. [Hallazgo de mayor severidad]
File: [ruta/relativa/archivo.ext]
Approximate line: [número]

### Issue & Impact
[Explicación técnica del problema y su riesgo]

### Current Vulnerable/Inefficient Code
```
[código actual]
```

### Recommended Production Code
```
[código corregido u optimizado]
```

# RECOMMENDED ACTION PLAN
## Fase 1 (Inmediato - Correcciones Críticas y de Seguridad)
1. [Acción 1]
2. [Acción 2]

## Fase 2 (Corto Plazo - Refactorización y Limpieza de Duplicación)
1. [Acción 1]

## Fase 3 (Mediano Plazo - Arquitectura y Rendimiento)
1. [Acción 1]"""
    )
}


def get_analysis_mode_config(mode_key: str) -> AnalysisModeConfig:
    """Returns the AnalysisModeConfig for the given mode key, defaulting to MODE_PROBLEM."""
    k = mode_key.strip().lower() if mode_key else MODE_PROBLEM
    if k in ANALYSIS_MODES:
        return ANALYSIS_MODES[k]
    return ANALYSIS_MODES[MODE_PROBLEM]
