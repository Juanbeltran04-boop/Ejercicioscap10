# Análisis Sintáctico LL(1) en Python

Este repositorio contiene un ejercicio de análisis sintáctico basado en el algoritmo LL(1). El objetivo es analizar una gramática libre de contexto (CFG), calcular los conjuntos **Primeros**, **Siguientes** y **Predicción**, y verificar si la gramática es **LL(1)**. El ejercicio está dividido en dos scripts: uno para la gramática y otro para el análisis sintáctico.

## Requisitos

Para ejecutar este ejercicio, necesitas tener Python instalado en tu máquina. Este código fue desarrollado y probado en Python 3.x, pero debería funcionar en versiones recientes de Python sin problemas.

### Requisitos del sistema:
- **Python 3.x**
- Ninguna librería externa es necesaria, ya que el código solo depende de la biblioteca estándar de Python.

## Estructura del Proyecto

El proyecto se divide en dos scripts:

1. **gramatica.py**: Aquí se define la gramática a analizar. Este archivo contiene las producciones de la gramática que se desea analizar (como en el ejemplo dado con las reglas `I → J uno`, `I → dos K`, etc.).
   
2. **analisis.py**: Este script contiene el código para calcular los conjuntos de **Primeros**, **Siguientes**, **Predicción** y verificar si la gramática es **LL(1)**. Este archivo es el que realiza el análisis y la verificación de la gramática.

### Ejemplo de los archivos:

#### gramatica.py:
```python
gramatica = {
    "I": [["J", "uno"], ["dos", "K"], ["ε"]],
    "X": [["I", "tres", "J", "K"], ["cuatro"], ["ε"]],
    "J": [["X", "cinco", "K", "seis"], ["ε"]],
    "K": [["siete", "X"], ["ε"]],
}
### la gramatica es LL(1) o no y porque.
La gramática no es LL(1) porque las producciones de S→B uno y S→dos C tienen un conflicto en sus conjuntos FIRST (comparten el terminal 'dos').
