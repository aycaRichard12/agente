==============================================================
REPORTED PROBLEM OR GOAL / PROBLEMA REPORTADO U OBJETIVO
==============================================================
quiero optimizar el codigo


==============================================================
SELECTED ANALYSIS PROFILE / PERFIL DE ANÁLISIS: 🐞 Detect errors
==============================================================
• Objetivo: Identificar errores de sintaxis, bugs lógicos, excepciones no controladas, condiciones de carrera y fallos de tipo en el código.
• Enfoque: Detección exhaustiva de bugs, casos límite (edge cases), seguridad de nulos/undefined, control de flujo y manejo robusto de excepciones.
• Prioridades: 1. Crashes y errores que detienen la ejecución. 2. Fallos silenciosos y corrupción de estado. 3. Manejo deficiente de excepciones. 4. Regresiones potenciales.
• Resultado esperado: Localización exacta de cada error (archivo y línea), causa raíz técnica, código corregido listo para copiar/pegar y caso de prueba de verificación.

⚠️ REGLA DE CONCRECIÓN TÉCNICA: El análisis debe ser CONCRETO, TÉCNICO y ORIENTADO A LA ACCIÓN. Concéntrate exclusivamente en fallos reproducibles y errores verificables. Omite comentarios estilísticos o divagaciones teóricas que no resuelvan un error.

==============================================================
PROJECT CONTEXT / CONTEXTO DEL PROYECTO
==============================================================
• Nombre del Proyecto: cm
• Ruta Base: /media/richard/Nuevo vol/quasar/dess/cm
• Fecha de Generación: 2026-09-24 17:31:37

--------------------------------------------------------------
PROJECT SUMMARY
--------------------------------------------------------------
Selected files: 1
File extensions:
  .php: 1

Total lines:
134

--------------------------------------------------------------
INSTRUCCIONES OBLIGATORIAS PARA DEEPSEEK (DETECT ERRORS)
--------------------------------------------------------------
El análisis debe ser CONCRETO, TÉCNICO y ORIENTADO A LA ACCIÓN. Concéntrate exclusivamente en fallos reproducibles y errores verificables. Omite comentarios estilísticos o divagaciones teóricas que no resuelvan un error.

Tu respuesta DEBE seguir exactamente la siguiente estructura Markdown adaptada al perfil:

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

REGLA OBLIGATORIA: No respondas con JSON. Responde con el Markdown estructurado exacto indicado arriba.

Estructura de Directorios:
```
cm/
└── db/
    └── conexion copy.php
```


==============================================================
ATTACHMENTS / ARCHIVOS Y CÓDIGO FUENTE
==============================================================

==============================================================
FILE: db/conexion copy.php
==============================================================
```php
LINE   1 | <?php
LINE   2 | // conexion.php — Fábrica de conexiones con Singleton + Lazy Loading
LINE   3 | //
LINE   4 | // PROBLEMA RESUELTO:
LINE   5 | // Cada clase (ventas, funciones, compras...) hacía "new Conexion()" por separado,
LINE   6 | // abriendo múltiples grupos de conexiones por petición y superando el límite de
LINE   7 | // Hostinger → error 2002 "Operation not permitted".
LINE   8 | //
LINE   9 | // SOLUCIÓN:
LINE  10 | // Singleton: todas las clases comparten la MISMA instancia de Conexion.
LINE  11 | // Lazy loading: cada BD se conecta solo cuando se necesita por primera vez.
LINE  12 | // Resultado: máximo 4 conexiones MySQL por petición (em, ad, cm, rh),
LINE  13 | // sin importar cuántas clases PHP instancien "Conexion::getInstance()".
LINE  14 | 
LINE  15 | require_once __DIR__ . "/bd.php";
LINE  16 | 
LINE  17 | class Conexion {
LINE  18 | 
LINE  19 |     // ── Singleton ─────────────────────────────────────────────────────────────
LINE  20 |     private static ?Conexion $instance = null;
LINE  21 | 
LINE  22 |     /**
LINE  23 |      * Retorna la única instancia de Conexion para esta petición.
LINE  24 |      * Usar siempre Conexion::getInstance() en lugar de new Conexion().
LINE  25 |      */
LINE  26 |     public static function getInstance(): self {
LINE  27 |         if (self::$instance === null) {
LINE  28 |             self::$instance = new self();
LINE  29 |         }
LINE  30 |         return self::$instance;
LINE  31 |     }
LINE  32 | 
LINE  33 |     // Constructor privado — impide "new Conexion()" desde fuera
LINE  34 |     private function __construct() {}
LINE  35 | 
LINE  36 |     // ── Instancias internas (null = no conectado aún) ─────────────────────────
LINE  37 |     private ?BDyofinanciero $_em = null;
LINE  38 |     private ?BDyofinanciero $_ad = null;
LINE  39 |     private ?BDyofinanciero $_cm = null;
LINE  40 |     private ?BDyofinanciero $_rh = null;
LINE  41 |     private ?BDyofinanciero $_prod = null;
LINE  42 | 
LINE  43 |     // Endpoints de facturación electrónica
LINE  44 |     public array $endPoint = [
LINE  45 |         1 => "https://sinfel.emizor.com",
LINE  46 |         2 => "https://fel.emizor.com",
LINE  47 |         3 => "https://mistersofts.com",
LINE  48 |     ];
LINE  49 | 
LINE  50 |     // ── Lazy getters ──────────────────────────────────────────────────────────
LINE  51 | 
LINE  52 |     public function getEm(): BDyofinanciero {
LINE  53 |         if ($this->_em === null) {
LINE  54 |             $this->_em = new BDyofinanciero(
LINE  55 |                 "esfalsoloscredenciales",
LINE  56 |                 "@esfalsoloscredenciales",
LINE  57 |                 "esfalsoloscredenciales"
LINE  58 |             );
LINE  59 |         }
LINE  60 |         return $this->_em;
LINE  61 |     }
LINE  62 | 
LINE  63 |     public function getAd(): BDyofinanciero {
LINE  64 |         if ($this->_ad === null) {
LINE  65 |             $this->_ad = new BDyofinanciero(
LINE  66 |                 "esfalsoloscredenciales",
LINE  67 |                 "@esfalsoloscredenciales#esfalsoloscredenciales",
LINE  68 |                 "esfalsoloscredenciales"
LINE  69 |             );
LINE  70 |         }
LINE  71 |         return $this->_ad;
LINE  72 |     }
LINE  73 | 
LINE  74 |     public function getCm(): BDyofinanciero {
LINE  75 |         if ($this->_cm === null) {
LINE  76 |             $this->_cm = new BDyofinanciero(
LINE  77 |                 "esfalsoloscredenciales",
LINE  78 |                 "@esfalsoloscredenciales#2025",
LINE  79 |                 "esfalsoloscredenciales"
LINE  80 |             );
LINE  81 |         }
LINE  82 |         return $this->_cm;
LINE  83 |     }
LINE  84 | 
LINE  85 |     public function getRh(): BDyofinanciero {
LINE  86 |         if ($this->_rh === null) {
LINE  87 |             $this->_rh = new BDyofinanciero(
LINE  88 |                 "esfalsoloscredenciales",
LINE  89 |                 "@esfalsoloscredenciales#234",
LINE  90 |                 "esfalsoloscredenciales"
LINE  91 |             );
LINE  92 |         }
LINE  93 |         return $this->_rh;
LINE  94 |     }
LINE  95 |     public function getProd(): BDyofinanciero {
LINE  96 |         if ($this->_prod === null) {
LINE  97 |             $this->_prod = new BDyofinanciero(
LINE  98 |                 "esfalsoloscredenciales",
LINE  99 |                 "@esfalsoloscredenciales",
LINE 100 |                 "esfalsoloscredenciales"
LINE 101 |             );
LINE 102 |         }
LINE 103 |         return $this->_prod;
LINE 104 |     }
LINE 105 | 
LINE 106 |     // ── Acceso por propiedad (compatibilidad con código existente) ─────────────
LINE 107 |     // Permite $conexion->cm, $conexion->em, etc. sin cambiar las clases de negocio.
LINE 108 |     public function __get(string $name): ?BDyofinanciero {
LINE 109 |         return match($name) {
LINE 110 |             'em' => $this->getEm(),
LINE 111 |             'ad' => $this->getAd(),
LINE 112 |             'cm' => $this->getCm(),
LINE 113 |             'rh' => $this->getRh(),
LINE 114 |             'prod' => $this->getProd(),
LINE 115 |             default => null,
LINE 116 |         };
LINE 117 |     }
LINE 118 | 
LINE 119 |     // ── Cierre explícito de conexiones ────────────────────────────────────────
LINE 120 |     public function closeAll(): void {
LINE 121 |         foreach (['_em', '_ad', '_cm', '_rh', '_prod'] as $prop) {
LINE 122 |             if ($this->$prop !== null) {
LINE 123 |                 $this->$prop->close();
LINE 124 |                 $this->$prop = null;
LINE 125 |             }
LINE 126 |         }
LINE 127 |     }
LINE 128 | 
LINE 129 |     // Prevenir clonación y deserialización del singleton
LINE 130 |     private function __clone() {}
LINE 131 |     public function __wakeup(): void {
LINE 132 |         throw new \Exception("No se puede deserializar un Singleton.");
LINE 133 |     }
LINE 134 | }
```