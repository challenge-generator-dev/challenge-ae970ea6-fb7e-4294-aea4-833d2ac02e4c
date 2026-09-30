# AGENTS.md

Instrucciones para el agente de IA que abra este repositorio (Claude Code, Cursor, Codex, Copilot, Gemini). Se cargan solas: no hay que pegar nada en ningun chat.

## Que es este repositorio

Es el codigo base de un reto de aprendizaje de Pragma: **Creación de un programa simple en Python**.

| | |
|---|---|
| Tema | python |
| Nivel | trainee-l1 |
| Chapter | Backend |
| Especialidad | Python |
| Stack | Python / n/a |
| Patron arquitectonico | script estructurado con funciones |
| Tiempo estimado | 1 hora |

## Receta del stack

Esqueleto obligatorio:

- `pyproject.toml o requirements.txt en la raiz`
- `app/main.py con la instancia de FastAPI`
- `app/domain con entidades y puertos (Protocol o ABC)`
- `app/application con casos de uso`
- `app/infrastructure con repositorios y routers`

Dependencias:

- Python 3.12

## Tu tarea

Dejar este proyecto en estado **verificable**: que el comando de verificacion corra sin errores. Escribi los archivos en disco, en este repositorio. No generes ZIPs ni archivos adjuntos.

En orden:

1. Corre `pip install -r src/requirements.txt && python -c "import app.main"` y mira que falla.
2. Completa lo que falte de la lista de abajo: manifiesto de dependencias, punto de entrada, capa de interfaz y las capas del patron declarado.
3. Arregla SOLO los errores que impiden compilar o arrancar.
4. Volve a correr `pip install -r src/requirements.txt && python -c "import app.main"` hasta que pase.
5. Pará ahí.

## Regla dura: las fases son trabajo del humano

**PROHIBIDO implementar los entregables de las fases.** El valor del reto esta en que la persona los resuelva. Tu trabajo es que tenga un proyecto que arranca; el hueco pedagogico se queda como esta.

No resuelvas nada de esto:

- **Fase 1 — Ingreso y validación de transacciones**: Programa que permite al usuario ingresar transacciones y las almacena en una lista si pasan la validación.
- **Fase 2 — Mostrar transacciones registradas**: Programa que permite al usuario ingresar transacciones, valida los datos de entrada y muestra todas las transacciones registradas al final.

Distincion operativa:

- **Arreglar** (si): import faltante, tipo que no existe, dependencia sin declarar, error de sintaxis, archivo referenciado que no existe.
- **No tocar** (no): logica de negocio incompleta, validaciones ausentes, secretos hardcodeados, APIs deprecadas que funcionan, concurrencia insegura, patrones mejorables. Eso es lo que la persona tiene que encontrar.

## Lo que falta y tenes que completar

### 1. Boilerplate del stack (1)

Sin esto el proyecto no compila ni arranca. **Es tu trabajo crearlo**, y no toca nada de lo pedagogico: es andamiaje del stack.

- [ ] **__init__.py** — Sin __init__.py, app no es un paquete importable y "import app.main" falla.

### Presentes (5)

- `__init__.py`
- `main.py`
- `src/requirements.txt`
- `src/transacciones.py`
- `src/README.md`

### Capas del patron declarado

Cada una tiene que existir como directorio real con al menos un archivo. Codigo plano en la raiz no satisface el patron.

- `src`

## Verificacion

```bash
pip install -r src/requirements.txt && python -c "import app.main"
```

Ese comando pasando es la definicion de "terminado" para vos.

## Convenciones que tenes que respetar

- Un solo ecosistema: no declares librerias de otro lenguaje ni mezcles gestores de paquetes.
- Toda libreria que uses tiene que estar declarada en el manifiesto de dependencias.
- Todo import declarado tiene que usarse; todo tipo usado tiene que existir o venir de una dependencia declarada.
- El patron es **script estructurado con funciones**: los contratos (interfaces, puertos) los define la capa interna y los implementa la externa, nunca al revés.
- Los archivos que crees llevan implementacion real, no stubs: sin `TODO`, sin cuerpos vacios, sin `// getters y setters`.

## Contexto del candidato

Sirve para calibrar el nivel del codigo, no para resolver las fases.

- Brecha que el reto ataca: Hacer un programa simple con Python

---

*Generado por Challenge Generator — Pragma. `README.md` tiene el enunciado completo del reto para la persona. `PROMPT_MEJORA.md` es la variante para pegar en un chat, si se prefiere ese flujo.*
