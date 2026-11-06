# Matriz antisimétrica

## Descripción del ejercicio

Crear una función en Python que determine si una matriz es antisimétrica.

Una matriz cuadrada es antisimétrica cuando se cumple:

`matriz[i][j] == -matriz[j][i]`

Para todas las posiciones de la matriz.

La función `esAntisimetrica(matriz)` devuelve:

- `True` si la matriz es antisimétrica.
- `False` si no cumple la condición o no es cuadrada.

## Solución desarrollada

```python
def esAntisimetrica(matriz):

    for fila in matriz:
        if len(fila) != len(matriz):
            return False

    antisimetrica = True

    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] != -matriz[j][i]:
                antisimetrica = False

    return antisimetrica
```

## Cómo funciona

**1. Comprobar que la matriz sea cuadrada**

```python
for fila in matriz:
    if len(fila) != len(matriz):
        return False
```

Una matriz cuadrada tiene tantas filas como columnas.

Se comprueba que cada fila tenga el mismo número de elementos que filas tiene la matriz.

Si alguna no cumple esta condición, la función devuelve `False` inmediatamente.

**2. Recorrer las posiciones de la matriz**

```python
for i in range(len(matriz)):
    for j in range(len(matriz[i])):
```

Utilizamos dos bucles `for` anidados:

- `i` representa el índice de la fila.
- `j` representa el índice de la columna.

Esto permite acceder a cada elemento mediante `matriz[i][j]`.

**3. Comprobar la antisimetría**

```python
if matriz[i][j] != -matriz[j][i]:
    antisimetrica = False
```

Se compara cada elemento con el opuesto de su posición transpuesta.

Si alguna pareja no cumple la condición, la matriz no es antisimétrica.

**4. Devolver el resultado**

```python
return antisimetrica
```

La variable comienza siendo `True` y cambia a `False` cuando se detecta un incumplimiento.

## Pruebas realizadas

Se han utilizado seis pruebas mediante `assert`:

| Caso | Resultado esperado |
|---|---|
| Matriz de ceros 3 × 3 | `True` |
| Matriz antisimétrica 3 × 3 | `True` |
| Matriz con elementos que incumplen la condición | `False` |
| Matriz triangular con diagonal distinta de cero | `False` |
| Matriz no cuadrada 3 × 4 | `False` |
| Matriz no cuadrada 1 × 9 | `False` |

## Qué he aprendido

### Matrices como listas de listas

En Python puedo representar una matriz utilizando una lista que contiene otras listas.

```python
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
```

### Acceso mediante dos índices

- `matriz[i]` permite acceder a una fila.
- `matriz[i][j]` permite acceder a un elemento concreto.
- `matriz[j][i]` permite acceder a la posición con los índices intercambiados.

### Uso de `len()` y `range()`

He practicado cómo obtener el número de filas, recorrer sus índices y comprobar la longitud de cada fila.

### Bucles anidados

He aprendido a utilizar un `for` dentro de otro para recorrer las posiciones de una matriz.

### Variables booleanas

He utilizado una variable inicializada en `True` que cambia a `False` cuando una condición deja de cumplirse.

### Diferencia entre `print()` y `return`

- `print()` muestra información en pantalla.
- `return` devuelve un valor y finaliza la ejecución de la función.

### Control de errores

He aprendido por qué aparece `IndexError: list index out of range` cuando intento acceder a una posición inexistente y cómo evitarlo comprobando previamente las dimensiones.

### Pruebas con `assert`

He utilizado `assert` para comprobar automáticamente que la función devuelve los resultados esperados.

### Ejecución con `__name__ == "__main__"`

He separado la definición de la función de las pruebas, de manera que estas se ejecuten cuando inicio directamente el archivo.

## Posibles mejoras

- Finalizar inmediatamente con `return False` cuando se detecta una pareja incorrecta.
- Evitar comprobaciones repetidas de posiciones simétricas.
- Añadir pruebas para matrices vacías y matrices de diferentes tamaños.
- Incorporar anotaciones de tipos.

## Conclusión

Este ejercicio me ha permitido comprender cómo recorrer matrices mediante índices y cómo traducir una condición matemática a instrucciones de Python.

La principal dificultad fue distinguir entre recorrer los valores de una matriz y recorrer sus índices, además de comprobar que la matriz fuese cuadrada antes de acceder a posiciones intercambiadas.