# Analizador Sintáctico con Bison y Flex

## 1. ¿Qué vamos a hacer?

En este proyecto vamos a construir un **analizador sintáctico** que verifica si una cadena ingresada por el usuario cumple con una **gramática específica**. Para ello, usaremos dos herramientas clásicas en compiladores:

- **Flex**, para el análisis léxico (identificación de palabras clave como "uno", "dos", etc.).
- **Bison**, para el análisis sintáctico (validación de estructuras según reglas gramaticales).

Cuando se ejecute el programa, le pedirá al usuario que ingrese una cadena. Si la cadena cumple con la gramática definida, mostrará el mensaje `"Cadena válida."`, y si no, indicará un **error de sintaxis**.

---

## 2. ¿Qué necesitamos? (Requisitos)

Para compilar y ejecutar este proyecto necesitas:

- Un sistema Linux (recomendado Kali Linux)
- Tener instaladas las siguientes herramientas:

```bash
sudo apt update
sudo apt install bison flex build-essential
