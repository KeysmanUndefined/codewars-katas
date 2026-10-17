# Permute a Palindrome

Ejercicio de Python basado en el kata **Permute a Palindrome** de Codewars.

## Enunciado

Crear una función que determine si los caracteres de una cadena pueden reorganizarse para formar un **palíndromo**.

Un palíndromo se lee igual de izquierda a derecha que de derecha a izquierda.

| Entrada | Resultado |
|---|---|
| `"madam"` | `True` |
| `"adamm"` | `True` |
| `"junk"` | `False` |
| `""` | `True` |

## Mi solución

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

## Cómo funciona

La clave es que **una cadena puede reorganizarse como palíndromo si, como máximo, un carácter aparece un número impar de veces**.

La función recorre los caracteres distintos mediante `set()`, cuenta sus apariciones con `.count()` y utiliza el operador módulo `%` para identificar las frecuencias impares. Finalmente, devuelve un booleano según el número de caracteres con frecuencia impar.

**Nota:** esta implementación elimina los espacios antes de comprobar la cadena. Si los espacios deben contar como caracteres en el kata, habría que retirar `replace(" ", "")`.

## Explicación paso a paso

El cuaderno Jupyter (`.ipynb`) contiene el desarrollo completo del ejercicio y explicaciones de los conceptos empleados, entre ellos:

- Cadenas de texto y valores booleanos.
- Funciones, bucles `for` y condiciones `if`.
- `set()`, `.count()` y `.replace()`.
- Operador módulo `%` y comparaciones.
- Precedencia de operadores.
- `return` e indentación.

**[Consultar el notebook con la explicación completa](./Palindromo.ipynb)**

## Autor

[KeysmanUndefined](https://github.com/KeysmanUndefined) · [Repositorio de Codewars Katas](https://github.com/KeysmanUndefined/codewars-katas)
