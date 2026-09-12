"""
Analysis Types and Profiles for DeepSeek prompt customization.
Defines 10 specialized analysis profiles that dynamically shape the LLM prompt's:
- Objective
- Focus
- Priorities
- Expected Outcome
- Structured Response Template
"""
from dataclasses import dataclass
from typing import Dict, List, Optional


@dataclass
class AnalysisProfile:
    name: str
    display_name: str
    icon: str
    objective: str
    focus: str
    priorities: str
    expected_outcome: str
    default_prompt_hint: str
    response_instructions: str
    response_template: str


ANALYSIS_PROFILES: Dict[str, AnalysisProfile] = {
    "Detect errors": AnalysisProfile(
        name="Detect errors",
        display_name="Detect errors (Detectar errores)",
        icon="🐞",
        objective="Identificar errores de sintaxis, bugs lógicos, excepciones no controladas, condiciones de carrera y fallos de tipo en el código.",
        focus="Detección exhaustiva de bugs, casos límite (edge cases), seguridad de nulos/undefined, control de flujo y manejo robusto de excepciones.",
        priorities="1. Crashes y errores que detienen la ejecución. 2. Fallos silenciosos y corrupción de estado. 3. Manejo deficiente de excepciones. 4. Regresiones potenciales.",
        expected_outcome="Localización exacta de cada error (archivo y línea), causa raíz técnica, código corregido listo para copiar/pegar y caso de prueba de verificación.",
        default_prompt_hint="Por favor audita y detecta todos los errores, excepciones no controladas, fallos lógicos o condiciones de carrera presentes en el código adjunto.",
        response_instructions="El análisis debe ser CONCRETO, TÉCNICO y ORIENTADO A LA ACCIÓN. Concéntrate exclusivamente en fallos reproducibles y errores verificables. Omite comentarios estilísticos o divagaciones teóricas que no resuelvan un error.",
        response_template="""# DIAGNOSIS
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
[Prueba o caso límite para verificar que el bug fue resuelto]"""
    ),

    "Solve problem": AnalysisProfile(
        name="Solve problem",
        display_name="Solve problem (Resolver problema)",
        icon="🔧",
        objective="Diagnosticar la causa raíz y resolver quirúrgicamente el problema específico reportado por el desarrollador.",
        focus="Solución directa, eficaz y de mínimo impacto colateral para la incidencia descrita.",
        priorities="1. Causa raíz del síntoma reportado. 2. Corrección quirúrgica y mantenible. 3. Preservación estricta de la funcionalidad adyacente.",
        expected_outcome="Diagnóstico directo, archivos exactos a modificar con líneas aproximadas, código de sustitución listo y plan de implementación paso a paso.",
        default_prompt_hint="Tengo el siguiente problema en el proyecto: [Describe aquí el error exacto, mensaje de excepción o comportamiento inesperado que deseas resolver].",
        response_instructions="El análisis debe ser CONCRETO, TÉCNICO y ORIENTADO A LA ACCIÓN. Enfócate exclusivamente en resolver el problema reportado de raíz, sin desviarte a refactorizaciones no solicitadas.",
        response_template="""# DIAGNOSIS
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
2. [Paso 2]"""
    ),

    "Refactoring": AnalysisProfile(
        name="Refactoring",
        display_name="Refactoring (Refactorización)",
        icon="♻️",
        objective="Simplificar, limpiar y estructurar el código existente para mejorar su legibilidad, mantenibilidad y reducir deuda técnica sin alterar su comportamiento externo.",
        focus="Eliminación de duplicación (DRY), reducción de complejidad ciclomática, desacoplamiento, nombres expresivos y adopción de modismos limpios del lenguaje.",
        priorities="1. Métodos y clases gigantes (God classes/functions). 2. Código duplicado. 3. Anidamiento excesivo. 4. Mejoras de legibilidad con contratos idénticos.",
        expected_outcome="Comparativa de código antes/después con explicaciones de la mejora aplicada, asegurando compatibilidad 100% con el comportamiento existente.",
        default_prompt_hint="Por favor revisa el código para refactorizarlo: simplificar lógica compleja, eliminar código duplicado, mejorar la legibilidad y aplicar buenas prácticas sin alterar la funcionalidad externa.",
        response_instructions="El análisis debe ser CONCRETO, TÉCNICO y ORIENTADO A LA ACCIÓN. Concéntrate en transformaciones de código medibles que reduzcan la deuda técnica. No alteres la interfaz pública ni los contratos existentes.",
        response_template="""# REFACTORING DIAGNOSIS
## Code Smells & Debt
[Lista de puntos críticos de deuda técnica, duplicación o complejidad excesiva]

# REFACTORED FILES
## 1. [ruta/relativa/archivo.ext]
Approximate line: [número]
### Target Smell
[Smell o problema de diseño corregido]
### Before Refactor
```
[código original complejo o duplicado]
```
### After Refactor
```
[código refactorizado limpio y desacoplado]
```
### Improvements Achieved
- Complejidad ciclomática reducida
- Cohesión mejorada

# CONTRACT PRESERVATION CHECK
[Confirmación de que los contratos y comportamientos existentes se mantienen intactos]"""
    ),

    "Improve architecture": AnalysisProfile(
        name="Improve architecture",
        display_name="Improve architecture (Mejorar arquitectura)",
        icon="🏛️",
        objective="Evaluar y optimizar la estructura global del sistema, límites modulares, separación de responsabilidades y patrones de diseño para máxima escalabilidad.",
        focus="Principios SOLID, Clean/Hexagonal Architecture, inyección de dependencias, límites de capas y organización coherente de módulos.",
        priorities="1. Acoplamiento indebido entre capas. 2. Dependencias circulares. 3. Fuga de detalles de infraestructura al dominio. 4. Escalabilidad modular.",
        expected_outcome="Diagnóstico de dependencias y límites, propuesta de redistribución de módulos/capas, interfaces desacopladas y plan de migración arquitectónica.",
        default_prompt_hint="Por favor evalúa la arquitectura general del proyecto. Propón mejoras en la separación de capas, desacoplamiento de componentes, inyección de dependencias y organización estructural.",
        response_instructions="El análisis debe ser CONCRETO, TÉCNICO y ORIENTADO A LA ACCIÓN. Enfócate en estructura, capas, límites modulares y contratos entre componentes. Evita filosofías abstractas sin soporte de código concreto.",
        response_template="""# ARCHITECTURAL ASSESSMENT
## Current Bottlenecks & Violations
[Análisis de acoplamientos indebidos, dependencias circulares o violación de capas]

## Target Architecture
[Diseño propuesto de capas, módulos y flujo de dependencias]

# STRUCTURAL & COMPONENT CHANGES
## 1. [Interfaces / Abstracciones clave]
```
[código de interfaces o contratos desacoplados]
```

## 2. [Modificaciones a módulos existentes]
### [ruta/relativa/archivo.ext]
Approximate line: [número]
```
[código reestructurado alineado a la nueva arquitectura]
```

# NEW FILES & DIRECTORY REORGANIZATION
[Estructura de carpetas o nuevos archivos requeridos para la arquitectura]

# MIGRATION STRATEGY
1. [Paso 1 de migración gradual sin romper el sistema]
2. [Paso 2]"""
    ),

    "Optimize performance": AnalysisProfile(
        name="Optimize performance",
        display_name="Optimize performance (Optimizar rendimiento)",
        icon="⚡",
        objective="Detectar cuellos de botella de latencia, uso ineficiente de memoria, operaciones bloqueantes y sobrecarga computacional en CPU e I/O.",
        focus="Complejidad algorítmica (Big-O), alocaciones innecesarias, I/O bloqueante, consultas redundantes, sincronismo evitable y fugas de memoria.",
        priorities="1. Bucles críticos y operaciones de alta frecuencia. 2. Operaciones I/O no asíncronas o no indexadas. 3. Reducción de huella de memoria. 4. Caching y computación perezosa.",
        expected_outcome="Análisis de complejidad temporal/espacial, reemplazo quirúrgico de código ineficiente por alternativas de alto rendimiento y directrices de benchmarking.",
        default_prompt_hint="Por favor analiza el rendimiento del código adjunto: detecta cuellos de botella de CPU, memoria, operaciones de entrada/salida o algoritmos lentos, y proporciona optimizaciones concretas de alto impacto.",
        response_instructions="El análisis debe ser CONCRETO, TÉCNICO y ORIENTADO A LA ACCIÓN. Justifica cada optimización con impacto en complejidad temporal (Big-O) o uso de memoria. No sugieras micro-optimizaciones que sacrifiquen legibilidad sin beneficio real.",
        response_template="""# PERFORMANCE BOTTLENECKS
## Identified Hotspots
[Lista técnica de cuellos de botella identificados con su impacto estimado]

# CODE OPTIMIZATIONS
## 1. [ruta/relativa/archivo.ext]
Approximate line: [número]
### Bottleneck
[Operación costosa: complejidad actual O(...), consumo de memoria, bloqueo I/O]
### Current Inefficient Code
```
[código lento actual]
```
### High-Performance Optimized Code
```
[código optimizado de alto rendimiento: O(...)]
```
### Benchmark & Impact
- Complejidad antes vs después
- Reducción esperada en latencia o consumo

# CACHING & CONCURRENCY RECOMMENDATIONS
[Estrategias de paralelismo, concurrencia o cache si aplican]"""
    ),

    "Review security": AnalysisProfile(
        name="Review security",
        display_name="Review security (Revisión de seguridad)",
        icon="🛡️",
        objective="Auditar el código en busca de vulnerabilidades de seguridad, vectores de explotación, fugas de datos y violaciones a estándares OWASP.",
        focus="Inyecciones (SQLi, XSS, Command Injection), autenticación, autorización, validación de inputs, deserialización insegura y exposición de secretos.",
        priorities="1. Vulnerabilidades críticas explotables remotamente. 2. Exposición de credenciales/tokens. 3. Falla en control de accesos. 4. Endurecimiento de configuraciones.",
        expected_outcome="Matriz de vulnerabilidades con severidad (Crítica/Alta/Media/Baja), vector de ataque, parche de mitigación en código y recomendaciones preventivas.",
        default_prompt_hint="Por favor realiza una auditoría de seguridad exhaustiva en el código: detecta vulnerabilidades OWASP, fallos de inyección, autenticación, autorización, manejo de datos sensibles y provee los parches de seguridad correspondientes.",
        response_instructions="El análisis debe ser CONCRETO, TÉCNICO y ORIENTADO A LA ACCIÓN. Describe con precisión el vector de ataque y provee el parche exacto para neutralizar la vulnerabilidad de inmediato.",
        response_template="""# SECURITY AUDIT
## Vulnerability Summary
| Vulnerabilidad | Severidad | Vector de Ataque | Archivo |
|---|---|---|---|
| [Nombre] | [Crítica/Alta/Media/Baja] | [Vector] | [Ruta] |

# VULNERABILITY REMEDIATION
## 1. [Nombre de la vulnerabilidad]
Severity: [Crítica / Alta / Media / Baja]
File: [ruta/relativa/archivo.ext]
Approximate line: [número]

### Attack Vector & Risk
[Cómo puede explotarse y qué impacto tiene]

### Vulnerable Code
```
[código vulnerable actual]
```

### Secured Remediation Patch
```
[código seguro con validación, escape o mitigación aplicada]
```

# HARDENING & SECURE BEST PRACTICES
[Medidas preventivas complementarias en configuración o dependencias]"""
    ),

    "Create new functionality": AnalysisProfile(
        name="Create new functionality",
        display_name="Create new functionality (Crear nueva funcionalidad)",
        icon="✨",
        objective="Diseñar e implementar una nueva funcionalidad o módulo respetando la arquitectura, patrones y convenciones del proyecto existente.",
        focus="Diseño no invasivo, interfaces claras, flujo de datos coherente, extensión limpia de modelos y servicios existentes sin romper compatibilidad.",
        priorities="1. Integración natural con la base de código actual. 2. Completitud funcional del requerimiento. 3. Cero regresiones en código existente.",
        expected_outcome="Especificación técnica de la funcionalidad, código completo listo para producción de los nuevos archivos y modificaciones precisas a los existentes.",
        default_prompt_hint="Deseo agregar la siguiente nueva funcionalidad al proyecto: [Describe detalladamente la característica que deseas construir, entradas esperadas y resultado requerido].",
        response_instructions="El análisis debe ser CONCRETO, TÉCNICO y ORIENTADO A LA ACCIÓN. Proporciona código funcional completo para producción, no pseudo-código ni fragmentos incompletos con '// resto del código'.",
        response_template="""# FEATURE SPECIFICATION
## Requirements & Scope
[Descripción técnica de la nueva funcionalidad]

## Architecture Integration
[Cómo se conecta con los modelos, servicios y controladores existentes]

# NEW FILES TO CREATE
## 1. [ruta/relativa/nuevo_archivo.ext]
Purpose: [Propósito del archivo]
```
[código fuente completo listo para producción]
```

# MODIFICATIONS TO EXISTING FILES
## 1. [ruta/relativa/archivo_existente.ext]
Approximate line: [número]
### Integration Point
[Punto exacto de integración]
### Modified Code
```
[código modificado con la integración de la nueva característica]
```

# USAGE EXAMPLE & TESTING
```
[ejemplo concreto de invocación o prueba de la nueva funcionalidad]
```"""
    ),

    "Explain project": AnalysisProfile(
        name="Explain project",
        display_name="Explain project (Explicar proyecto)",
        icon="📖",
        objective="Proporcionar una explicación técnica integral, rigurosa y pedagógica del funcionamiento, flujo de datos y arquitectura del proyecto.",
        focus="Ciclo de vida de la ejecución, responsabilidades de cada módulo/capa, flujo de información de entrada a salida y abstracciones clave.",
        priorities="1. Flujo de ejecución principal desde los entry points. 2. Rol y responsabilidad de cada componente. 3. Manejo de estado y persistencia.",
        expected_outcome="Explicación técnica estructurada, diagrama o descripción del flujo de datos, desglose de componentes clave y guía para nuevos desarrolladores.",
        default_prompt_hint="Por favor explica en profundidad este proyecto: su propósito principal, arquitectura general, flujo de datos desde los puntos de entrada y el rol de cada módulo clave.",
        response_instructions="El análisis debe ser CONCRETO, TÉCNICO y ORIENTADO A LA ACCIÓN. Concéntrate en la realidad técnica del código adjunto sin inventar suposiciones. No propongas código de refactorización innecesario.",
        response_template="""# PROJECT OVERVIEW
## Core Purpose & Tech Stack
[Qué hace el proyecto, tecnologías clave y problema que resuelve]

# ARCHITECTURE & DESIGN
## Structural Breakdown
[Organización de carpetas, capas y módulos principales con sus responsabilidades]

## Key Abstractions
[Clases, servicios o componentes centrales y cómo interactúan]

# EXECUTION FLOW & DATA PIPELINE
1. [Punto de entrada: inicio del ciclo de vida]
2. [Paso intermedio: procesamiento o lógica de negocio]
3. [Salida: respuesta, persistencia o interfaz gráfica]

# KEY EXTENSION POINTS
[Dónde y cómo debe un desarrollador extender el proyecto si desea añadir funciones]"""
    ),

    "Document project": AnalysisProfile(
        name="Document project",
        display_name="Document project (Documentar proyecto)",
        icon="📝",
        objective="Generar documentación técnica profesional, estandarizada y completa para APIs, módulos, docstrings y guía de uso del proyecto.",
        focus="Firmas de funciones/métodos, tipos de entrada/salida, descripciones de parámetros, excepciones arrojadas, ejemplos de uso y README técnico.",
        priorities="1. Interfaces públicas no documentadas. 2. Servicios de negocio críticos. 3. Endpoints o contratos de API. 4. Guía de instalación y ejecución.",
        expected_outcome="Docstrings estándar (Google/Sphinx/JSDoc/PHPDoc) listos para integrar, documentación de API en Markdown y guía técnica para el repositorio.",
        default_prompt_hint="Por favor genera documentación técnica completa para el proyecto: docstrings profesionales para funciones/clases clave, especificaciones de tipos, ejemplos de uso y una guía técnica estructurada.",
        response_instructions="El análisis debe ser CONCRETO, TÉCNICO y ORIENTADO A LA ACCIÓN. Genera documentación directamente utilizable con ejemplos de código ejecutables y especificaciones de tipos rigurosas.",
        response_template="""# PROJECT DOCUMENTATION
## Executive Technical Summary
[Resumen conciso del sistema para desarrolladores]

# API & COMPONENT REFERENCE
## 1. [Componente / Servicio / Módulo]
File: [ruta/relativa/archivo.ext]

### Methods & Functions
#### `nombreFuncion(param1: Tipo, param2: Tipo) -> Retorno`
- **Descripción**: [Propósito claro]
- **Parámetros**:
  - `param1`: [descripción y restricciones]
  - `param2`: [descripción]
- **Retorno**: [tipo y significado]
- **Excepciones**: [errores potenciales]
- **Ejemplo**:
```
[código de ejemplo de llamada]
```

# READY-TO-PASTE DOCSTRINGS
## [ruta/relativa/archivo.ext]
```
[bloque con los docstrings listos para insertar en el archivo]
```

# ENVIRONMENT & SETUP GUIDE
[Variables requeridas, comandos de instalación y pasos de despliegue]"""
    ),

    "Comprehensive review": AnalysisProfile(
        name="Comprehensive review",
        display_name="Comprehensive review (Revisión integral)",
        icon="🔍",
        objective="Realizar una auditoría técnica 360° que evalúe errores, vulnerabilidades de seguridad, calidad arquitectónica, rendimiento y mantenibilidad.",
        focus="Balance global de la salud de ingeniería de software del proyecto, identificando desde bugs inmediatos hasta mejoras estructurales estratégicas.",
        priorities="1. Errores críticos y vulnerabilidades de seguridad. 2. Cuellos de botella graves de rendimiento. 3. Puntos neurálgicos de refactorización. 4. Plan de acción por fases.",
        expected_outcome="Matriz holística de hallazgos categorizados por impacto/urgencia, correcciones quirúrgicas inmediatas y hoja de ruta de mejoras recomendadas.",
        default_prompt_hint="Por favor realiza una revisión integral 360° del proyecto: analiza errores, seguridad, arquitectura, rendimiento y calidad de código, entregando una matriz de hallazgos priorizados y correcciones listas para aplicar.",
        response_instructions="El análisis debe ser CONCRETO, TÉCNICO y ORIENTADO A LA ACCIÓN. Prioriza los hallazgos por severidad y provee soluciones específicas con código listo para producción.",
        response_template="""# COMPREHENSIVE 360° AUDIT MATRIX
| Categoría | Severidad | Hallazgo Técnico | Archivo Afectado |
|---|---|---|---|
| Bugs | Alta/Med/Baja | [Descripción] | [Ruta] |
| Seguridad | Alta/Med/Baja | [Descripción] | [Ruta] |
| Rendimiento | Alta/Med/Baja | [Descripción] | [Ruta] |
| Arquitectura | Alta/Med/Baja | [Descripción] | [Ruta] |

# CRITICAL & HIGH PRIORITY FIXES
## 1. [Nombre del hallazgo prioritario]
File: [ruta/relativa/archivo.ext]
Approximate line: [número]
### Current Code
```
[código problemático]
```
### Corrected Production Code
```
[código corregido y seguro]
```

# ARCHITECTURAL & QUALITY ENHANCEMENTS
[Recomendaciones estructurales clave y desacoplamiento]

# ACTIONABLE ROADMAP
- **Fase 1 (Inmediato)**: Parchear bugs críticos y seguridad.
- **Fase 2 (Corto plazo)**: Optimizar cuellos de botella y refactorizar componentes acoplados.
- **Fase 3 (Mediano plazo)**: Fortalecer pruebas y documentación."""
    )
}

# Ordered list of keys matching user request exactly
ANALYSIS_TYPE_KEYS: List[str] = [
    "Detect errors",
    "Solve problem",
    "Refactoring",
    "Improve architecture",
    "Optimize performance",
    "Review security",
    "Create new functionality",
    "Explain project",
    "Document project",
    "Comprehensive review",
]


def get_analysis_profile(key: str) -> AnalysisProfile:
    """Returns the AnalysisProfile for a given key, falling back to 'Detect errors'."""
    if key in ANALYSIS_PROFILES:
        return ANALYSIS_PROFILES[key]
    # Check case-insensitive match
    k_lower = key.strip().lower()
    for k, profile in ANALYSIS_PROFILES.items():
        if k.lower() == k_lower or profile.display_name.lower() == k_lower:
            return profile
    return ANALYSIS_PROFILES["Detect errors"]


def get_all_analysis_types() -> List[str]:
    """Returns list of canonical analysis type names."""
    return list(ANALYSIS_TYPE_KEYS)
