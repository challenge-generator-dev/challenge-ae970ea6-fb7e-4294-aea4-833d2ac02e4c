# Prompt para Mejorar el Codigo Base

Copia y pega el contenido del bloque de abajo en un asistente de IA (Claude, ChatGPT)
para obtener un ZIP con el proyecto completo y arrancable.

Si preferis trabajar en tu editor con un agente local (Claude Code, Cursor, Copilot), usa `AGENTS.md` en vez de este archivo: dice lo mismo pero para que escriba los archivos en disco.

## Las dos reglas que no se negocian

1. **Completa el boilerplate.** Todo lo que el proyecto necesita para compilar y arrancar: manifiesto de dependencias, punto de entrada, configuracion, capa de interfaz, y las capas del patron arquitectonico declarado. Eso es andamiaje y es tu trabajo.
2. **NO resuelvas el reto.** Los entregables de las fases son el trabajo de la persona. El hueco pedagogico se deja como esta: el proyecto arranca, pero lo que el reto pide implementar NO esta implementado.

Dicho de otra forma: si algo impide compilar, arreglalo. Si algo es logica de negocio incompleta, validaciones ausentes, un secreto hardcodeado o un patron mejorable, dejalo exactamente como esta — es lo que la persona tiene que encontrar.

## Lo que le falta a este proyecto

Esto NO lo tenes que adivinar: salio de comparar el proyecto contra la arquitectura declarada del reto y de un analisis estatico del codigo. Completalo TODO.

### Boilerplate del stack que falta

Sin esto no compila ni arranca. Es andamiaje, no toca nada de lo pedagogico:

- **__init__.py** — Sin __init__.py, app no es un paquete importable y "import app.main" falla.

## Como saber que terminaste

```bash
pip install -r src/requirements.txt && python -c "import app.main"
```

Ese comando corriendo sin errores es la definicion de "listo".

---

```
## Briefing del reto (autoridad)
Este bloque manda sobre los archivos adjuntos. El stack y el rol salen de AQUÍ, no de un topic genérico ni de markdown placeholder.

### Contexto técnico original
Hacer un programa simple con Python

### Reto
- Tema: python
- Seniority: trainee-l1
- Tipo: practical
- Título: Creación de un programa simple en Python
- Tiempo estimado: 1 hora

### Fases (trabajo del HUMANO — PROHIBIDO completarlas)
No implementes estos entregables. Dejalos como hueco pedagógico. El asistente solo materializa el proyecto arrancable para que el participante pueda trabajar.
- Fase 1: Ingreso y validación de transacciones — objetivo: Permitir al usuario ingresar transacciones y validar los datos de entrada. — entregable (NO resolver): Programa que permite al usuario ingresar transacciones y las almacena en una lista si pasan la validación.
- Fase 2: Mostrar transacciones registradas — objetivo: Mostrar al usuario todas las transacciones registradas. — entregable (NO resolver): Programa que permite al usuario ingresar transacciones, valida los datos de entrada y muestra todas las transacciones registradas al final.

Eres un asistente experto en análisis, corrección y generación de archivos de cualquier tipo:
código fuente, documentación, hojas de cálculo, documentos Word, configuraciones, entre otros.
Voy a enviarte una cadena de texto que contiene uno o más archivos. Cada archivo está delimitado por un marcador con el siguiente formato:
// === ARCHIVO: ruta/del/archivo.extension ===
o también puede aparecer como:
## === ARCHIVO: ruta/del/archivo.extension ===
Lo que sigue al marcador puede ser:

El contenido real del archivo (código, texto, YAML, etc.)
Una descripción en lenguaje natural de lo que debe contener el archivo


TU TAREA
PASO 0 — ¿Esto es un proyecto o una carcasa?
Antes de extraer archivos, leé el Briefing (si está) y diagnosticá el adjunto.

Es CARCASA si ocurre CUALQUIERA de estas:
- No hay manifiesto de dependencias del stack del briefing (manifest.json de VTEX IO / package.json / pom.xml / build.gradle / requirements.txt / go.mod / *.tf / *.csproj, según corresponda)
- Hay un "binario" que en realidad es un comentario ("no puede ser mostrado como texto plano", placeholder .fig/.docx vacío)
- Los markdowns ya completan entregables de fases posteriores ("se implementó fade-in", lista de áreas ya resuelta)

Si es CARCASA:
- MATERIALIZÁ un proyecto que arranca en el stack del briefing (VTEX IO Store Framework, Angular, Terraform, pytest, Nest, etc.). Incluí manifiesto, punto de entrada y capa de interfaz reales.
- NO copies los markdowns de "solución" como si fueran el producto. Son ruido de generación.
- NO resuelvas las fases del briefing (están marcadas PROHIBIDO). Dejá el hueco pedagógico: el flujo existe, las microinteracciones/calidad/infra que el reto pide NO están hechas.
- Después seguí al PASO 5 (ZIP).

Si es un proyecto REAL (manifiesto + código que compila o arranca):
- Seguí PASO 1 en adelante. 🔴 compilación sí. 🟡 pedagógico no.

PASO 1 — Detección y extracción
Identifica todos los archivos presentes en la cadena. Para cada archivo extrae:

Su ruta completa (ej: src/main/java/com/pragma/Service.java)
Su contenido o descripción

PASO 2 — Clasificación por tipo
Clasifica cada archivo en una de estas categorías:
A) Código fuente (Java, Python, TypeScript, JavaScript, Kotlin, etc.)
B) Configuración / documentación (YAML, properties, Markdown, JSON, txt, etc.)
C) Excel (.xlsx, .xls, .csv)
D) Word (.docx, .doc)
E) Otro tipo de archivo binario o especial
PASO 3 — Clasificación de errores en código fuente

Objetivo prioritario: que el proyecto compile. No corrijas flujo de negocio ni lógica funcional.

Antes de modificar cualquier archivo de código fuente, clasifica cada problema encontrado en una de estas dos categorías:
🔴 ERROR DE COMPILACIÓN — corregir siempre
Son errores que impiden que el proyecto arranque, sin valor pedagógico:

Import faltante o incorrecto
Clase, método o variable referenciada que no existe en ningún archivo del proyecto
Error de sintaxis
Anotación con atributos inválidos
Dependencia ausente en pom.xml, package.json, etc.
Archivo referenciado que no existe y debe ser creado con implementación mínima

→ CORREGIR estos errores.
🟡 PROBLEMA FUNCIONAL O DE CALIDAD — preservar siempre
Son problemas que no impiden compilar. Pueden ser intencionales para el aprendizaje:

Clave secreta hardcodeada ("secret", "password123")
API deprecada que funciona pero tiene reemplazo moderno
Lógica de negocio incorrecta o incompleta
Código redundante o de baja legibilidad
Falta de validaciones en flujo de negocio
Patrones de diseño incorrectos pero funcionales
Concurrencia no segura
Configuración funcional pero no óptima

→ PRESERVAR tal cual. No corregir, no mejorar, no comentar.
PASO 4 — Procesamiento según tipo de archivo
Tipo A — Código fuente
Aplica únicamente las correcciones clasificadas como 🔴 ERROR DE COMPILACIÓN.
No alteres ningún elemento clasificado como 🟡 PROBLEMA FUNCIONAL O DE CALIDAD.
Si falta un archivo referenciado, créalo con la implementación mínima necesaria para compilar.
Tipo B — Configuración / documentación
Extrae el contenido tal cual, sin modificaciones salvo errores evidentes de sintaxis
(ej: YAML mal indentado).
Tipo C — Excel (.xlsx)
Si viene con contenido real, genera el archivo respetando ese contenido.
Si viene con descripción en lenguaje natural, genera un archivo Excel funcional con:

Fila de encabezados en negrita con color de fondo distintivo
Columnas con ancho ajustado al contenido
Tipos de dato correctos por columna
Validaciones si la descripción lo indica
Hojas nombradas descriptivamente si hay más de una
Filas de ejemplo si no hay datos reales

Tipo D — Word (.docx)
Si viene con contenido real, genera el archivo respetando ese contenido.
Si viene con descripción en lenguaje natural, genera un documento Word funcional con:

Estilos de título (Título 1, Título 2) para jerarquía de secciones
Fuente legible (Calibri o equivalente), tamaño 11-12pt para cuerpo
Márgenes estándar
Tabla de contenido si tiene múltiples secciones
Tablas con encabezados en negrita si aplica

Tipo E — Otro
Genera el archivo con el contenido o estructura más apropiada según la descripción.
PASO 5 — Exportación en ZIP
Empaqueta todos los archivos en un único archivo ZIP descargable respetando exactamente
la estructura de rutas indicada por los marcadores.
El ZIP debe incluir:

Archivos de código con únicamente los errores de compilación corregidos
Archivos de configuración y documentación sin cambios
Archivos nuevos creados para resolver dependencias de compilación faltantes
Archivos Excel y Word generados desde descripción

IMPORTANTE: El ZIP debe estar listo para descargar al finalizar. No preguntes si el usuario
quiere generarlo. Simplemente genera el archivo y proporciona el enlace de descarga; No debes desplegar en el chat el resumen de lo que arreglaste al Zip, solo entregalo.

REGLAS IMPORTANTES

No omitas ningún archivo aunque no tenga errores ni modificaciones
Respeta los nombres y rutas exactas indicadas por los marcadores
Si un archivo no tiene marcador claro, infiere el nombre desde su contenido
Si la cadena contiene solo documentación, placeholders o binarios fake, NO la reproduzcas:
aplicá PASO 0 (materializar el proyecto del briefing). Reproducir la carcasa es un fallo.
No agregues texto después del enlace de descarga del ZIP
No preguntes si el usuario quiere el ZIP: simplemente generalo siempre
Si detectas que falta un archivo de configuración necesario para compilar
(pom.xml, package.json, requirements.txt, build.gradle, etc.), créalo e inclúyelo
inferiendo su contenido desde los imports y frameworks detectados en el código
Nunca corrijas problemas 🟡 aunque parezcan obvios o fáciles de mejorar.
El participante que recibirá este proyecto los debe encontrar y resolver él mismo.


INPUT
Aquí está la cadena con los archivos:

// === ARCHIVO: __init__.py ===
# Este archivo marca el directorio como un paquete Python.
# Permite importaciones como "from app import main" o "import app.transacciones".

__all__ = ['main', 'transacciones']

// === ARCHIVO: main.py ===

# Programa de gestión de transacciones bancarias
# Este script permite registrar transacciones con monto y descripción,
# validando que el monto sea positivo y la descripción no esté vacía.
# Finalmente, muestra todas las transacciones registradas.

def validar_transaccion(monto: float, descripcion: str) -> bool:
    """
    Valida que el monto sea positivo y la descripción no esté vacía.
    Args:
        monto: Monto de la transacción.
        descripcion: Descripción de la transacción.
    Returns:
        bool: True si la transacción es válida, False en caso contrario.
    """
    return monto > 0 and descripcion.strip() != ""

def registrar_transaccion(transacciones: list, monto: float, descripcion: str) -> None:
    """
    Registra una transacción en la lista de transacciones.
    Args:
        transacciones: Lista donde se almacenan las transacciones.
        monto: Monto de la transacción.
        descripcion: Descripción de la transacción.
    """
    transacciones.append({"monto": monto, "descripcion": descripcion})

def mostrar_transacciones(transacciones: list) -> None:
    """
    Muestra todas las transacciones registradas.
    Args:
        transacciones: Lista de transacciones registradas.
    """
    if not transacciones:
        print("No hay transacciones registradas.")
        return
    
    print("\nTransacciones registradas:")
    for idx, transaccion in enumerate(transacciones, start=1):
        print(f"{idx}. Monto: ${transaccion['monto']:.2f}, Descripción: {transaccion['descripcion']}")

def main() -> None:
    """
    Función principal que orquesta el flujo del programa.
    """
    transacciones = []
    
    print("Bienvenido al registro de transacciones bancarias.")
    print("Ingrese 'salir' en cualquier momento para terminar.")
    
    while True:
        descripcion = input("\nIngrese la descripción de la transacción: ").strip()
        
        if descripcion.lower() == "salir":
            break
            
        if descripcion == "":
            print("Error: La descripción no puede estar vacía.")
            continue
            
        try:
            monto = float(input("Ingrese el monto de la transacción: "))
        except ValueError:
            print("Error: El monto debe ser un número válido.")
            continue
            
        if not validar_transaccion(monto, descripcion):
            print("Error: El monto debe ser positivo y la descripción no puede estar vacía.")
            continue
            
        registrar_transaccion(transacciones, monto, descripcion)
        print("Transacción registrada con éxito.")
    
    mostrar_transacciones(transacciones)

if __name__ == "__main__":
    main()

// === ARCHIVO: src/requirements.txt ===
# Dependencias del proyecto
# Este archivo está vacío porque el proyecto no requiere librerías externas.


// === ARCHIVO: __init__.py ===
"""Paquete principal del sistema de gestión de transacciones bancarias.

Este módulo exporta las funciones principales para la gestión de transacciones.
"""

# Constantes del paquete
VERSION = "1.0.0"
NOMBRE_PAQUETE = "gestor_transacciones"
DESCRIPCION_PAQUETE = "Sistema de gestión de transacciones bancarias"

# Configuración de límites del sistema
MONTO_MINIMO = 0.01
MONTO_MAXIMO = 1000000.00
LONGITUD_MAXIMA_DESCRIPCION = 200
LONGITUD_MINIMA_DESCRIPCION = 1

# Mensajes del sistema
MENSAJE_ERROR_MONTO = "El monto debe ser un número positivo"
MENSAJE_ERROR_DESCRIPCION_VACIA = "La descripción no puede estar vacía"
MENSAJE_ERROR_DESCRIPCION_LARGA = f"La descripción no puede exceder {LONGITUD_MAXIMA_DESCRIPCION} caracteres"
MENSAJE_EXITO_TRANSACCION = "Transacción registrada exitosamente"
MENSAJE_ERROR_VALIDACION = "Error de validación: los datos proporcionados no son válidos"

# Título de la aplicación
TITULO_APP = "=" * 50
TITULO_APP += "\n  SISTEMA DE GESTIÓN DE TRANSACCIONES"
TITULO_APP += "\n" + "=" * 50


def obtener_configuracion() -> dict:
    """Retorna la configuración actual del paquete.
    
    Returns:
        dict: Diccionario con la configuración del paquete.
    """
    return {
        "version": VERSION,
        "nombre": NOMBRE_PAQUETE,
        "descripcion": DESCRIPCION_PAQUETE,
        "limites": {
            "monto_minimo": MONTO_MINIMO,
            "monto_maximo": MONTO_MAXIMO,
            "longitud_descripcion_max": LONGITUD_MAXIMA_DESCRIPCION,
            "longitud_descripcion_min": LONGITUD_MINIMA_DESCRIPCION
        }
    }


def validar_rango_monto(monto: float) -> bool:
    """Valida que el monto esté dentro del rango permitido.
    
    Args:
        monto: El monto a validar.
        
    Returns:
        bool: True si el monto está en el rango válido, False en caso contrario.
    """
    if not isinstance(monto, (int, float)):
        return False
    return MONTO_MINIMO <= monto <= MONTO_MAXIMO


def validar_longitud_descripcion(descripcion: str) -> bool:
    """Valida que la descripción tenga una longitud válida.
    
    Args:
        descripcion: La descripción a validar.
        
    Returns:
        bool: True si la longitud es válida, False en caso contrario.
    """
    if not isinstance(descripcion, str):
        return False
    longitud = len(descripcion.strip())
    return LONGITUD_MINIMA_DESCRIPCION <= longitud <= LONGITUD_MAXIMA_DESCRIPCION


def formatear_monto(monto: float) -> str:
    """Formatea un monto como cadena con formato monetario.
    
    Args:
        monto: El monto a formatear.
        
    Returns:
        str: El monto formateado con símbolo de moneda.
    """
    return f"${monto:,.2f}"


def limpiar_descripcion(descripcion: str) -> str:
    """Limpia una descripción eliminando espacios en blanco excesivos.
    
    Args:
        descripcion: La descripción a limpiar.
        
    Returns:
        str: La descripción limpia.
    """
    return " ".join(descripcion.split())


def crear_transaccion(monto: float, descripcion: str) -> dict:
    """Crea un diccionario representando una transacción.
    
    Args:
        monto: El monto de la transacción.
        descripcion: La descripción de la transacción.
        
    Returns:
        dict: Diccionario con los datos de la transacción.
    """
    return {
        "monto": monto,
        "descripcion": descripcion.strip()
    }


def obtener_mensaje_bienvenida() -> str:
    """Retorna el mensaje de bienvenida de la aplicación.
    
    Returns:
        str: Mensaje de bienvenida formateado.
    """
    return f"""
{TITULO_APP}

Versión: {VERSION}
{DESCRIPCION_PAQUETE}

"""


# Exportar funciones principales del paquete
__all__ = [
    "VERSION",
    "NOMBRE_PAQUETE",
    "obtener_configuracion",
    "validar_rango_monto",
    "validar_longitud_descripcion",
    "formatear_monto",
    "limpiar_descripcion",
    "crear_transaccion",
    "obtener_mensaje_bienvenida"
]

// === ARCHIVO: src/transacciones.py ===
"""Módulo de gestión de transacciones bancarias.

Este módulo contiene las funciones principales para validar, registrar
y mostrar transacciones bancarias.
"""

from typing import List, Dict, Optional

# Importar constantes del paquete principal
import sys
import os

# Agregar el directorio raíz al path para poder importar el paquete
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from __init__ import (
    MONTO_MINIMO,
    MONTO_MAXIMO,
    LONGITUD_MAXIMA_DESCRIPCION,
    MENSAJE_ERROR_MONTO,
    MENSAJE_ERROR_DESCRIPCION_VACIA,
    MENSAJE_ERROR_DESCRIPCION_LARGA,
    MENSAJE_EXITO_TRANSACCION,
    MENSAJE_ERROR_VALIDACION,
    TITULO_APP,
    formatear_monto,
    validar_rango_monto,
    validar_longitud_descripcion,
    crear_transaccion
)


def validar_transaccion(monto: float, descripcion: str) -> bool:
    """Valida que los datos de una transacción sean correctos.
    
    La validación verifica que:
    - El monto sea un número positivo mayor a cero.
    - La descripción no esté vacía y no exceda el límite de caracteres.
    
    Args:
        monto: El monto de la transacción a validar.
        descripcion: La descripción de la transacción.
        
    Returns:
        bool: True si la transacción es válida, False en caso contrario.
    """
    # Validar que el monto sea numérico
    if not isinstance(monto, (int, float)):
        print(f"Error: {MENSAJE_ERROR_MONTO}")
        return False
    
    # Validar que el monto sea positivo
    if monto <= 0:
        print(f"Error: {MENSAJE_ERROR_MONTO}")
        return False
    
    # Validar rango del monto
    if not validar_rango_monto(monto):
        print(f"Error: El monto debe estar entre {formatear_monto(MONTO_MINIMO)} y {formatear_monto(MONTO_MAXIMO)}")
        return False
    
    # Validar que la descripción no esté vacía
    if not descripcion or not descripcion.strip():
        print(f"Error: {MENSAJE_ERROR_DESCRIPCION_VACIA}")
        return False
    
    # Validar longitud de la descripción
    if not validar_longitud_descripcion(descripcion):
        print(f"Error: {MENSAJE_ERROR_DESCRIPCION_LARGA}")
        return False
    
    return True


def registrar_transaccion(transacciones: List[Dict], monto: float, descripcion: str) -> None:
    """Registra una nueva transacción en la lista de transacciones.
    
    Antes de registrar, valida que los datos sean correctos.
    
    Args:
        transacciones: Lista de transacciones donde se registrará la nueva.
        monto: El monto de la transacción.
        descripcion: La descripción de la transacción.
        
    Raises:
        ValueError: Si los datos de la transacción no son válidos.
    """
    # Validar la transacción antes de registrarla
    if not validar_transaccion(monto, descripcion):
        raise ValueError(MENSAJE_ERROR_VALIDACION)
    
    # Crear la transacción
    transaccion = crear_transaccion(monto, descripcion)
    
    # Agregar a la lista
    transacciones.append(transaccion)
    
    print(f"✓ {MENSAJE_EXITO_TRANSACCION}")
    print(f"  Monto: {formatear_monto(monto)}")
    print(f"  Descripción: {descripcion.strip()}")


def mostrar_transacciones(transacciones: List[Dict]) -> None:
    """Muestra todas las transacciones registradas en formato legible.
    
    Args:
        transacciones: Lista de transacciones a mostrar.
    """
    print("\n" + "=" * 50)
    print("  LISTADO DE TRANSACCIONES REGISTRADAS")
    print("=" * 50)
    
    if not transacciones:
        print("\nNo hay transacciones registradas.")
        print("=" * 50)
        return
    
    # Calcular total
    total = sum(t["monto"] for t in transacciones)
    
    # Mostrar cada transacción
    for indice, transaccion in enumerate(transacciones, start=1):
        monto = transaccion["monto"]
        descripcion = transaccion["descripcion"]
        
        print(f"\nTransacción #{indice}:")
        print(f"  Monto:      {formatear_monto(monto)}")
        print(f"  Descripción: {descripcion}")
    
    # Mostrar total
    print("\n" + "-" * 50)
    print(f"  TOTAL: {formatear_monto(total)}")
    print("=" * 50)
    print(f"  Cantidad de transacciones: {len(transacciones)}")
    print("=" * 50 + "\n")


def obtener_opcion_menu() -> str:
    """Muestra el menú de opciones y retorna la selección del usuario.
    
    Returns:
        str: La opción seleccionada por el usuario.
    """
    print("\n--- MENÚ DE OPCIONES ---")
    print("1. Registrar nueva transacción")
    print("2. Ver todas las transacciones")
    print("3. Salir")
    print("------------------------")
    
    return input("Seleccione una opción (1-3): ").strip()


def procesar_registro_transaccion(transacciones: List[Dict]) -> None:
    """Procesa el registro de una nueva transacción desde entrada del usuario.
    
    Args:
        transacciones: Lista de transacciones donde se registrará.
    """
    print("\n--- REGISTRAR TRANSACCIÓN ---")
    
    try:
        monto_str = input("Ingrese el monto: ").strip()
        monto = float(monto_str)
        
        descripcion = input("Ingrese la descripción: ").strip()
        
        registrar_transaccion(transacciones, monto, descripcion)
        
    except ValueError as e:
        print(f"Error al registrar transacción: {e}")
    except Exception as e:
        print(f"Error inesperado: {e}")


def ejecutar_menu_principal() -> None:
    """Ejecuta el menú principal de la aplicación.
    
    Controla el flujo principal del programa permitiendo al usuario
    registrar transacciones y ver el listado de las mismas.
    """
    transacciones: List[Dict] = []
    
    print("\n" + "=" * 50)
    print("  SISTEMA DE GESTIÓN DE TRANSACCIONES")
    print("=" * 50)
    print("\nBienvenido al sistema de gestión de transacciones.")
    print("Este programa le permite registrar y visualizar transacciones bancarias.")
    
    while True:
        opcion = obtener_opcion_menu()
        
        if opcion == "1":
            procesar_registro_transaccion(transacciones)
        elif opcion == "2":
            mostrar_transacciones(transacciones)
        elif opcion == "3":
            print("\nGracias por usar el sistema. ¡Hasta luego!")
            break
        else:
            print("\nOpción no válida. Por favor, seleccione 1, 2 o 3.")


def main() -> None:
    """Función principal del programa.
    
    Punto de entrada del sistema de gestión de transacciones.
    """
    ejecutar_menu_principal()


# Ejecutar el programa si se llama directamente
if __name__ == "__main__":
    main()

// === ARCHIVO: src/README.md ===
# Sistema de Gestión de Transacciones Bancarias

## Descripción del Proyecto

Este es un programa simple desarrollado en Python que permite gestionar un registro de transacciones bancarias. El sistema ofrece funcionalidades para validar, registrar y visualizar transacciones con monto y descripción.

## Dominio del Problema

El programa modela un escenario bancario básico donde:
- Los usuarios pueden ingresar transacciones con un monto y descripción
- Se valida que el monto sea positivo (mayor a cero)
- Se valida que la descripción no esté vacía y tenga una longitud máxima
- Las transacciones se almacenan en una lista en memoria
- Se puede visualizar el listado completo de transacciones registradas

## Estructura del Proyecto

```
├── __init__.py           # Paquete principal con configuración
├── main.py               # Punto de entrada del programa
└── src/
    ├── transacciones.py  # Módulo de lógica de transacciones
    └── README.md         # Este archivo
```

## Requisitos

- Python 3.12 o superior
- No requiere librerías externas adicionales

## Cómo Ejecutar

1. Asegúrate de tener Python 3.12 instalado:
   ```bash
   python --version
   ```

2. Ejecuta el programa desde la raíz del proyecto:
   ```bash
   python main.py
   ```

## Funcionalidades

### 1. Registro de Transacciones
- Ingresa el monto de la transacción (número positivo)
- Ingresa una descripción (texto no vacío, máximo 200 caracteres)
- El sistema valida los datos antes de guardar

### 2. Visualización de Transacciones
- Muestra todas las transacciones registradas
- Incluye el número, monto y descripción de cada una
- Muestra el total acumulado de todas las transacciones
- Indica la cantidad total de transacciones

### 3. Validación de Datos
- **Monto**: Debe ser un número positivo entre $0.01 y $1,000,000.00
- **Descripción**: No puede estar vacía y debe tener entre 1 y 200 caracteres

## Menú de Opciones

El programa presenta un menú interactivo con las siguientes opciones:
- **1**: Registrar nueva transacción
- **2**: Ver todas las transacciones
- **3**: Salir del programa

## Convenciones del Código

El código sigue estas convenciones:
- Uso de funciones para separar responsabilidades
- Validación de datos de entrada con mensajes claros
- Almacenamiento en lista de diccionarios con claves 'monto' y 'descripcion'
- Formato legible para mostrar transacciones usando f-strings
- Tipado estático con annotations de Python

## Errores Comunes y Soluciones

### Error: "El monto debe ser un número positivo"
- Causa: Se intentó ingresar un monto cero, negativo o no numérico
- Solución: Ingrese un monto mayor a cero

### Error: "La descripción no puede estar vacía"
- Causa: Se intentó registrar una transacción sin descripción
- Solución: Ingrese una descripción válida

### Error: "La descripción no puede exceder 200 caracteres"
- Causa: La descripción ingresada es demasiado larga
- Solución: Reduzca la longitud de la descripción

## Autor

Programa desarrollado como ejercicio de aprendizaje de Python.

```
