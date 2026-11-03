
# Permute a Palindrome

## Contexto

Este proyecto resuelve el kata **Permute a Palindrome** de Codewars.

El objetivo es determinar si los caracteres de una cadena de texto pueden reorganizarse para formar un palíndromo.

Un **palíndromo** es una secuencia de caracteres que se lee igual de izquierda a derecha que de derecha a izquierda.

No es necesario generar todas las permutaciones posibles. Basta con analizar cuántas veces aparece cada carácter.

Para que exista una permutación palindrómica, **como máximo un carácter puede aparecer un número impar de veces**.

## Instalación y configuración

### Requisitos previos

- Python 3.11 o superior.
- Visual Studio Code (opcional).
- Extensión Jupyter para ejecutar el notebook.

### Ejecución

El ejercicio puede ejecutarse directamente en Python o mediante el archivo `Palindromo.ipynb`.

## Implementación

La solución utiliza una función que recibe una cadena de texto y devuelve un valor booleano (`True` o `False`).

```python
def permute_a_palindrome(input):

    impares = 0
    input = input.replace(" ", "")

    for letra in set(input):
        contador = input.count(letra)

        if contador % 2 != 0:
            impares += 1

    return impares <= 1
```

El algoritmo sigue estas etapas:

1. **Inicialización:** se crea un contador para registrar cuántos caracteres aparecen un número impar de veces.
2. **Tratamiento de espacios:** se eliminan los espacios de la cadena.
3. **Identificación de caracteres:** `set()` obtiene los caracteres únicos.
4. **Recuento:** `.count()` calcula las apariciones de cada carácter.
5. **Comprobación:** el operador `%` determina si la frecuencia es impar.
6. **Resultado:** se devuelve `True` cuando existe, como máximo, un carácter con frecuencia impar.

## Resultados

| Entrada | Resultado |
|---|---|
| `"madam"` | `True` |
| `"adamm"` | `True` |
| `"junk"` | `False` |
| `"aabbc"` | `True` |
| `"aabbcd"` | `False` |
| `""` | `True` |

La solución evita generar permutaciones y utiliza funciones integradas de Python para analizar los caracteres.

## Documentación

El notebook contiene una explicación detallada del desarrollo del ejercicio, incluyendo:

- Uso de `set()` y `.count()`.
- Operador módulo `%`.
- Condicionales y operadores de comparación.
- Precedencia de operadores en Python.
- Funcionamiento de `return`.
- Ejemplos y pruebas del algoritmo.

[Consultar Palindromo.ipynb](https://github.com/KeysmanUndefined/codewars-katas/blob/main/Palindromo/Palindromo.ipynb)

## Referencias

- Codewars — *Permute a Palindrome*.
- [Documentación oficial de Python](https://docs.python.org/3/).

## Autor

**KeysmanUndefined**

Repositorio de ejercicios de programación en Python y Codewars.
