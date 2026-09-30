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