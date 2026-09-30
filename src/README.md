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