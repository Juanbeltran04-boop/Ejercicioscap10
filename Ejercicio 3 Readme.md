# Analizador Sintáctico Descendente Recursivo (ASDR) en Python

Este proyecto implementa un analizador sintáctico descendente recursivo (ASDR) para una gramática específica. El objetivo principal es demostrar el funcionamiento de un analizador predictivo que intenta derivar una cadena de entrada a partir del símbolo inicial de la gramática, utilizando un conjunto de funciones recursivas, donde cada función corresponde a una no terminal de la gramática. A través de este ejercicio, se exploran los conceptos de gramáticas libres de contexto, producciones gramaticales y el proceso de análisis sintáctico descendente.

## 🛠️ Requisitos

Para ejecutar este analizador, necesitarás tener instalado lo siguiente en tu sistema:

1.  **Python 3:** El código está escrito en Python 3. Puedes verificar tu instalación abriendo una terminal o línea de comandos y ejecutando:
    ```bash
    python3 --version
    ```
    Si no tienes Python 3 instalado, puedes descargarlo desde [python.org](https://www.python.org/).

2.  **Editor de Texto (Opcional):** Aunque no es estrictamente necesario para ejecutar el código, un editor de texto facilitará la visualización y posible modificación del archivo `.py`. Puedes usar opciones como VS Code, Sublime Text, Atom, o incluso editores más simples como `nano` o `gedit`.

## 🚀 Compilación y Ejecución

Dado que Python es un lenguaje interpretado, no requiere un paso de compilación explícito. Para ejecutar el analizador:

1.  **Guarda el código:** Asegúrate de haber guardado el código del analizador en un archivo con extensión `.py` (por ejemplo, `analizador_original.py`).

2.  **Abre la terminal:** Abre la terminal o línea de comandos de tu sistema operativo.

3.  **Navega al directorio:** Utiliza el comando `cd` para navegar hasta el directorio donde guardaste el archivo del analizador. Por ejemplo:
    ```bash
    cd /ruta/al/directorio
    ```

4.  **Ejecuta el script:** Ejecuta el analizador utilizando el intérprete de Python 3 con el siguiente comando:
    ```bash
    python3 analizador_original.py
    ```

5.  **Ingresa la entrada:** Al ejecutar el script, se te pedirá que ingreses la secuencia de tokens a analizar, separándolos con espacios. Por ejemplo:
    ```
    Ingrese la secuencia de tokens a analizar (separados por espacios): dos cuatro tres uno
    ```
    Presiona la tecla Enter para que el analizador procese la entrada.

6.  **Revisa la salida:** El analizador mostrará en la consola los pasos del análisis, indicando las no terminales que se están intentando y las coincidencias encontradas. Al final, informará si el análisis sintáctico fue exitoso o si se detectaron errores en la entrada según la gramática implementada.
