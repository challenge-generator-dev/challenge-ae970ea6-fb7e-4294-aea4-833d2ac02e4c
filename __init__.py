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