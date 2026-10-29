
# Is There a Vowel in There? — Codewars (8 kyu)

## Descripción

El ejercicio consiste en recibir una lista de números enteros y sustituir aquellos que representan vocales según el código ASCII.

| Código ASCII | Vocal |
|---|---|
| 97 | a |
| 101 | e |
| 105 | i |
| 111 | o |
| 117 | u |

Los demás números deben permanecer sin modificar.

### Ejemplo

```python
entrada = [101, 120, 105]
resultado = ["e", 120, "i"]
```

## Conceptos utilizados

### 1. Listas

Utilicé una lista vacía para almacenar los resultados.

```python
solucion = []
```

Aprendí que una lista puede contener elementos de distintos tipos, como `int` y `str`.

### 2. Bucle `for`

Utilicé un bucle para recorrer cada elemento de la lista.

```python
for i in inp:
```

Aprendí que `i` contiene el valor del elemento, no su posición.

### 3. Condicionales `if` y `elif`

Permiten comprobar si un número corresponde a una vocal.

```python
if i == 101:
    i = "e"
elif i == 117:
    i = "u"
```

### 4. Método `append()`

Permite añadir elementos al final de una lista.

```python
solucion.append(i)
```

Aprendí que `append()` modifica directamente la lista y devuelve `None`.

Por eso es incorrecto:

```python
solucion += solucion.append(i)
```

### 5. `return`

Devuelve el resultado de la función.

```python
return solucion
```

Aprendí que `return` termina inmediatamente la ejecución de una función.

### 6. Pruebas con `assert`

Utilicé `assert` para comprobar los resultados de la función.

```python
assert is_vow([101, 120, 105]) == ["e", 120, "i"]
```

Si el resultado no coincide, Python genera un `AssertionError`.

## Errores cometidos

### Error 1: Comparar una variable consigo misma

```python
if inp == inp:
    return inp
```

Esta condición siempre se cumple, por lo que el programa termina antes de ejecutar el bucle.

**Aprendizaje:** debo comprobar que las condiciones tengan sentido y entender cuándo se ejecuta `return`.

### Error 2: Confundir índice y valor

Inicialmente intenté utilizar:

```python
for i in inp:
    if numeros[indice] == 101:
```

Pero `indice` no estaba definido.

**Aprendizaje:** un `for` recorre directamente los valores. Si necesito también sus posiciones, puedo utilizar `enumerate()`.

### Error 3: Utilizar incorrectamente `append()`

Intenté:

```python
solucion += solucion.append(i)
```

**Aprendizaje:** `append()` ya modifica la lista. No necesita una asignación adicional.

### Error 4: Repetir código innecesariamente

Inicialmente escribía `solucion.append(i)` dentro de cada condición.

Descubrí que podía escribirlo una sola vez fuera de los condicionales, pero dentro del bucle.

## Solución final

```python
def is_vow(inp):
    solucion = []

    for i in inp:
        if i == 101:
            i = "e"
        elif i == 117:
            i = "u"
        elif i == 97:
            i = "a"
        elif i == 105:
            i = "i"
        elif i == 111:
            i = "o"

        solucion.append(i)

    return solucion
```

## Resumen de lo aprendido

- Recorrer listas con `for`.
- Utilizar condicionales `if` y `elif`.
- Trabajar con tipos `int` y `str` en una misma lista.
- Modificar el valor de una variable.
- Añadir elementos mediante `append()`.
- Utilizar `return` correctamente.
- Comprobar resultados con `assert`.
- Detectar errores lógicos.
- Evitar instrucciones repetidas.
- Comprender la relación entre códigos ASCII y caracteres.

## Posibles mejoras

Investigar otras formas de resolver el ejercicio:

- Utilizar un diccionario para relacionar números y vocales.
- Utilizar `chr()` para convertir códigos ASCII en caracteres.
- Comparar distintas soluciones para mejorar la legibilidad del código.

## Enlace al kata

[Is There a Vowel in There? — Codewars](https://www.codewars.com/kata/57cff961eca260b71900008f/train/python)
