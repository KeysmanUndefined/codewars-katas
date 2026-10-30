# Decode the Morse Code (6 kyu)

## 📌 Descripción

Ejercicio de [Codewars](https://www.codewars.com/kata/54b724efac3d5402db00065e) que consiste en traducir un mensaje escrito en código Morse a texto legible.

En el código Morse:

- Las letras están separadas por un espacio.
- Las palabras están separadas por tres espacios.
- El mensaje puede contener espacios adicionales al principio y al final.

El objetivo es desarrollar una función `decode_morse(morse_code)` que reciba una cadena en Morse y devuelva su traducción.

## 🛠️ Solución

```python
from preloaded import MORSE_CODE

def decode_morse(morse_code):

    resultado = ""
    palabras = morse_code.strip().split("   ")

    for palabra in palabras:
        for letra in palabra.split(" "):
            codigo = MORSE_CODE[letra]
            resultado += codigo

        resultado += " "

    return resultado.strip()
```

## 🧠 Explicación de la solución

### 1. Inicialización

```python
resultado = ""
```

Creo una cadena vacía donde voy guardando las letras traducidas.

### 2. Separación de palabras

```python
palabras = morse_code.strip().split("   ")
```

Utilizo `strip()` para eliminar los espacios iniciales y finales.

Después, con `split("   ")`, separo el mensaje en palabras utilizando los tres espacios que las delimitan.

### 3. Recorrido del mensaje

```python
for palabra in palabras:
    for letra in palabra.split(" "):
```

Utilizo dos bucles `for` anidados.

- El primer bucle recorre las palabras.
- El segundo recorre cada letra Morse dentro de la palabra, separándolas mediante `split(" ")`.

### 4. Traducción de las letras

```python
codigo = MORSE_CODE[letra]
resultado += codigo
```

Consulto el diccionario `MORSE_CODE` proporcionado por Codewars para obtener la letra correspondiente a cada secuencia Morse.

Después añado esa letra a la cadena `resultado`.

### 5. Separación de palabras

```python
resultado += " "
```

Al finalizar cada palabra, añado un espacio para separarla de la siguiente.

### 6. Resultado final

```python
return resultado.strip()
```

Devuelvo el mensaje traducido eliminando los espacios sobrantes de los extremos.

## 🧪 Ejemplo de ejecución

**Entrada:**

```python
".... . -.--   .--- ..- -.. ."
```

**Salida:**

```python
"HEY JUDE"
```

## 📚 Conceptos practicados

- Manipulación de cadenas de texto.
- Métodos `split()` y `strip()`.
- Bucles `for` anidados.
- Diccionarios y acceso a sus valores.
- Concatenación de cadenas.
- Funciones y `return`.

## 📂 Estructura del proyecto

```text
decode_morse/
├── src/
│   └── decode_morse.py
├── tests/
│   └── test_decode_morse.py
├── README.md
└── TESTING.md
```

## 🎯 Objetivo de aprendizaje

Practicar la manipulación de cadenas, el uso de diccionarios y los bucles anidados para resolver un problema de traducción de código Morse.

La solución se ha desarrollado utilizando estructuras básicas de Python, priorizando la comprensión del funcionamiento del código.