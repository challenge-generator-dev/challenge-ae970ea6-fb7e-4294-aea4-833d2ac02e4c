# Creación de un programa simple en Python

En el dominio de la banca, necesitas crear un programa que gestione un registro de transacciones. El programa debe permitir al usuario ingresar una transacción con monto y descripción, y almacenarla en una lista. El programa debe validar que el monto sea positivo y que la descripción no esté vacía. Al final, el programa debe mostrar todas las transacciones registradas.

## Informacion General

| Campo | Valor |
|-------|-------|
| **Tema** | python |
| **Nivel** | trainee-l1 |
| **Tipo** | practical |
| **Tiempo estimado** | 1 hora |

## Fases del Reto

### Fase 0: Configuración del Proyecto

**Objetivo:** Obtener el proyecto base funcional enviando el Código Base a un asistente de IA, que lo analizará, corregirá errores y generará un ZIP listo para usar.

**Tiempo estimado:** 15-30 minutos

**Instrucciones:**

- Asegúrate de tener instalado para ejecutar el proyecto: Python 3.10+, pip, VS Code o similar.
- Copia todo el contenido del campo **Código Base** de este reto — incluyendo el texto de instrucciones que aparece al inicio.
- Abre un asistente de IA (Claude en claude.ai, ChatGPT o Gemini — se recomienda Claude), pega el contenido copiado en el chat y envíalo.
- El asistente analizará los archivos, corregirá errores y generará un archivo ZIP descargable. Descárgalo y extráelo en la carpeta donde quieras trabajar.
- Ejecuta `pip install -r requirements.txt` y luego arranca el proyecto. Si no hay errores, estás listo.

**Entregable:** El proyecto compila/arranca sin errores.

<details>
<summary>Pistas de conocimiento</summary>

- Copia el Código Base completo incluyendo el texto de instrucciones al inicio — esas instrucciones le indican al asistente exactamente qué hacer con los archivos.
- Si el asistente no genera el ZIP automáticamente al terminar el análisis, escríbele: "genera el ZIP ahora".
- Si el proyecto tiene errores al arrancar, comparte el mensaje de error con el mismo asistente para que lo corrija.

</details>

### Fase 1: Ingreso y validación de transacciones

**Objetivo:** Permitir al usuario ingresar transacciones y validar los datos de entrada.

**Tiempo estimado:** 30 minutos

**Instrucciones:**

- Crea un programa que permita al usuario ingresar una transacción con monto y descripción.
- Valida que el monto sea positivo y que la descripción no esté vacía.
- Almacena la transacción en una lista si la validación es exitosa.

**Entregable:** Programa que permite al usuario ingresar transacciones y las almacena en una lista si pasan la validación.

<details>
<summary>Pistas de conocimiento</summary>

- Piensa en cómo puedes almacenar las transacciones de manera que sean accesibles posteriormente.
- Considera cómo puedes validar los datos de entrada de manera efectiva.

</details>

### Fase 2: Mostrar transacciones registradas

**Objetivo:** Mostrar al usuario todas las transacciones registradas.

**Tiempo estimado:** 30 minutos

**Instrucciones:**

- Modifica el programa para que muestre todas las transacciones registradas al final.
- Asegúrate de que la lista de transacciones se muestre de manera legible.

**Entregable:** Programa que permite al usuario ingresar transacciones, valida los datos de entrada y muestra todas las transacciones registradas al final.

<details>
<summary>Pistas de conocimiento</summary>

- Piensa en cómo puedes mostrar la lista de transacciones de manera legible.
- Considera cómo puedes asegurarte de que todas las transacciones se muestren correctamente.

</details>

## Dimensiones Evaluadas

- **queEs**: ¿Qué es una transacción en el contexto del programa?
- **paraQueSirve**: ¿Para qué sirve validar los datos de entrada en el programa?
- **comoSeUsa**: ¿Cómo se usa el programa para registrar transacciones?
- **erroresComunes**: ¿Cuáles son los errores comunes al ingresar transacciones y cómo los maneja el programa?

## Criterios de Evaluacion

- El programa permite al usuario ingresar transacciones y valida los datos de entrada.
- Las transacciones se almacenan en una lista si pasan la validación.
- El programa muestra todas las transacciones registradas al final.

## Como trabajar con un asistente de IA

Hay dos caminos, elegi uno:

- **AGENTS.md** (recomendado) — instrucciones nativas del repo. Abri esta carpeta con tu agente local (Claude Code, Cursor, Codex, Copilot, Gemini) y las carga solo. Sabe que archivos faltan y con que comando se verifica, y completa el scaffold escribiendo en disco.
- **PROMPT_MEJORA.md** — para copiar y pegar en un chat (claude.ai, ChatGPT). Devuelve un ZIP con el proyecto. Sirve si no tenes un agente en el IDE.

Ninguno de los dos resuelve las fases del reto: eso es tu trabajo.

## Verificacion

El proyecto esta listo para trabajar cuando este comando corre sin errores:

```bash
pip install -r src/requirements.txt && python -c "import app.main"
```

---

*Reto generado automaticamente por Challenge Generator - Pragma*
