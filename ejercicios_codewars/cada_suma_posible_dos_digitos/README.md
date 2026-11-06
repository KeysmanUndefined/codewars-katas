# Sumas de parejas de dígitos — Codewars

## 1. Descripción del ejercicio

**Plataforma:** Codewars  
**Lenguaje:** Python  
**Función:** `digits(n)`

El ejercicio consiste en recibir un número entero no negativo y devolver una lista con todas las posibles sumas de parejas de dígitos.

Las parejas deben generarse respetando el orden original de los dígitos, de izquierda a derecha, sin utilizar dos veces la misma posición ni repetir parejas en orden inverso.

### Ejemplo

**Entrada:**

```python
digits(12345)
```

**Salida esperada:**

```python
[3, 4, 5, 6, 5, 6, 7, 7, 8, 9]
```

Las operaciones realizadas son:

```text
1 + 2 = 3
1 + 3 = 4
1 + 4 = 5
1 + 5 = 6
2 + 3 = 5
2 + 4 = 6
2 + 5 = 7
3 + 4 = 7
3 + 5 = 8
4 + 5 = 9
```

## 2. Solución desarrollada

```python
def digits(n):

    n = str(n)
    resultado = []

    for i in range(len(n)):

        for j in range(i + 1, len(n)):

            resultado.append(int(n[i]) + int(n[j]))

    return resultado
```

## 3. Explicación del código

| Instrucción | Función |
|---|---|
| `def digits(n):` | Define una función que recibe el parámetro `n`. |
| `n = str(n)` | Convierte el número entero en una cadena para acceder a sus dígitos por posición. |
| `resultado = []` | Crea una lista vacía para almacenar las sumas. |
| `for i in range(len(n)):` | Recorre las posiciones de todos los dígitos. |
| `for j in range(i + 1, len(n)):` | Recorre las posiciones posteriores a `i`. |
| `int(n[i])` | Obtiene el dígito de la posición `i` y lo convierte a entero. |
| `int(n[j])` | Obtiene el dígito de la posición `j` y lo convierte a entero. |
| `resultado.append(...)` | Añade el resultado de la suma al final de la lista. |
| `return resultado` | Devuelve la lista con todas las sumas calculadas. |

### 3.1. Primer bucle `for`

```python
for i in range(len(n)):
```

Orden de ejecución:

1. `len(n)` obtiene la cantidad de caracteres.
2. `range(len(n))` genera una secuencia de índices desde `0` hasta `len(n) - 1`.
3. `for` asigna cada índice a la variable `i`.
4. Se ejecutan las instrucciones del interior del bucle.

Para `n = "12345"`, la variable `i` toma los valores `0, 1, 2, 3, 4`.

### 3.2. Segundo bucle `for`

```python
for j in range(i + 1, len(n)):
```

Este bucle recorre las posiciones situadas a la derecha de `i`.

Orden de ejecución:

1. `i + 1` calcula la posición siguiente a `i`.
2. `len(n)` obtiene el límite superior.
3. `range()` genera los índices comprendidos entre ambos valores, sin incluir el límite superior.
4. `j` toma cada índice generado y ejecuta la suma correspondiente.

**¿Por qué utilizamos `i + 1`?**

Porque evita utilizar dos veces la misma posición y repetir las parejas en orden inverso.

Por ejemplo, si ya hemos sumado `1 + 2`, no necesitamos realizar después `2 + 1`.

### 3.3. Método `append()`

```python
resultado.append(int(n[i]) + int(n[j]))
```

Esta instrucción obtiene dos dígitos, los convierte a enteros, realiza su suma y añade el resultado al final de la lista.

Ejemplo:

```python
resultado = []

resultado.append(3)
print(resultado)  # [3]

resultado.append(4)
print(resultado)  # [3, 4]

resultado.append(5)
print(resultado)  # [3, 4, 5]
```

El método `append()` conserva los elementos anteriores.

## 4. Tabla de ejecución paso a paso

Para `n = 12345`:

| Vuelta | `i` | `j` | `n[i]` | `n[j]` | Suma | Lista `resultado` |
|---|---|---|---|---|---|---|
| 1 | 0 | 1 | 1 | 2 | 3 | `[3]` |
| 2 | 0 | 2 | 1 | 3 | 4 | `[3, 4]` |
| 3 | 0 | 3 | 1 | 4 | 5 | `[3, 4, 5]` |
| 4 | 0 | 4 | 1 | 5 | 6 | `[3, 4, 5, 6]` |
| 5 | 1 | 2 | 2 | 3 | 5 | `[3, 4, 5, 6, 5]` |
| 6 | 1 | 3 | 2 | 4 | 6 | `[3, 4, 5, 6, 5, 6]` |
| 7 | 1 | 4 | 2 | 5 | 7 | `[3, 4, 5, 6, 5, 6, 7]` |
| 8 | 2 | 3 | 3 | 4 | 7 | `[3, 4, 5, 6, 5, 6, 7, 7]` |
| 9 | 2 | 4 | 3 | 5 | 8 | `[3, 4, 5, 6, 5, 6, 7, 7, 8]` |
| 10 | 3 | 4 | 4 | 5 | 9 | `[3, 4, 5, 6, 5, 6, 7, 7, 8, 9]` |

## 5. Tabla de ejecución del primer bucle

| `i` | Dígito seleccionado | Valores de `j` | Sumas realizadas | Número de sumas |
|---|---|---|---|---|
| 0 | 1 | 1, 2, 3, 4 | 1+2, 1+3, 1+4, 1+5 | 4 |
| 1 | 2 | 2, 3, 4 | 2+3, 2+4, 2+5 | 3 |
| 2 | 3 | 3, 4 | 3+4, 3+5 | 2 |
| 3 | 4 | 4 | 4+5 | 1 |
| 4 | 5 | Ninguno | Ninguna | 0 |

El primer bucle se ejecuta cinco veces, pero el segundo realiza cada vez menos iteraciones.

Cuando `i = 4`, el segundo bucle recibe `range(5, 5)`, que no contiene ningún índice.

Por tanto, no se ejecuta ninguna suma.

## 6. Pruebas de funcionamiento

```python
assert digits(12345) == [3, 4, 5, 6, 5, 6, 7, 7, 8, 9]

assert digits(123) == [3, 4, 5]

assert digits(12) == [3]

assert digits(5) == []

assert digits(0) == []

assert digits(111) == [2, 2, 2]
```

Estas pruebas permiten comprobar el comportamiento de la función con diferentes entradas, incluidos números de un solo dígito y dígitos repetidos.

## 7. Conceptos de Python utilizados

- **Funciones:** `def` y `return`.
- **Tipos de datos:** `int`, `str` y `list`.
- **Conversión de tipos:** `str()` e `int()`.
- **Longitud de secuencias:** `len()`.
- **Bucles anidados:** `for` dentro de otro `for`.
- **Generación de índices:** `range()`.
- **Acceso por posición:** `n[i]` y `n[j]`.
- **Métodos de listas:** `append()`.
- **Comprobación de resultados:** `assert`.

## 8. Conclusión

Con este kata he practicado el uso de bucles anidados para recorrer los dígitos de un número y generar todas las parejas posibles respetando su orden.

He utilizado la conversión de tipos para trabajar con los dígitos individualmente, el método `append()` para almacenar las sumas y `return` para devolver el resultado final.

La parte fundamental del ejercicio es comprender cómo se relacionan los índices `i` y `j`, y por qué el segundo bucle comienza en `i + 1`.

De esta manera se evita repetir parejas y se obtiene la lista de sumas solicitada.