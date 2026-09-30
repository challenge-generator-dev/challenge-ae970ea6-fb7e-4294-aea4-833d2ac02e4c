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