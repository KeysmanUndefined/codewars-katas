# Ecuación de segundo grado — TDD con pytest

## 1. Descripción

Proyecto desarrollado en Python para resolver ecuaciones de segundo grado mediante la metodología **TDD (Test-Driven Development)**, utilizando `pytest` para realizar pruebas automatizadas.

La ecuación general es:

**ax² + bx + c = 0**

El discriminante se calcula mediante:

**Δ = b² − 4ac**

Según el resultado:

- **Δ > 0:** dos soluciones reales distintas.
- **Δ = 0:** una solución real doble.
- **Δ < 0:** no existen soluciones reales.
- **a = 0:** se lanza una excepción `ValueError`, porque no es una ecuación de segundo grado.

## 2. Tecnologías utilizadas

- Python 3.13.3
- pytest 9.1.1
- Visual Studio Code
- Git y GitHub
- Entorno virtual `venv`

## 3. Estructura del proyecto

```text
ecuacion_segundo_grado/
├── images/
│   ├── Captura de pantalla 2026-10-15 212606.png
│   ├── Captura de pantalla 2026-10-15 212834.png
│   ├── Captura de pantalla 2026-10-15 213441.png
│   ├── Captura de pantalla 2026-10-15 213925.png
│   └── Captura de pantalla 2026-10-15 214543.png
├── src/
│   ├── __init__.py
│   └── ecuacion.py
├── test/
│   ├── __init__.py
│   └── test_ecuacion.py
├── pytest.ini
└── README.md
```

## 4. Desarrollo mediante TDD

El desarrollo se realizó siguiendo el ciclo:

**RED → GREEN → REFACTOR**

1. **RED:** escribir una prueba que falla.
2. **GREEN:** modificar el código para que la prueba pase.
3. **REFACTOR:** mejorar el código sin alterar su comportamiento.

### 4.1. Primera prueba: dos soluciones reales

Se comprueba la ecuación:

**x² − 5x + 6 = 0**

Soluciones esperadas: `(3, 2)`.

```python
def test_dos_soluciones():
    assert ecuacion2(1, -5, 6) == (3, 2)
```

Se comprueba que la función devuelve correctamente las dos soluciones mediante `return`.

![Primera prueba superada](<images/Captura de pantalla 2026-10-15 212606.png>)

### 4.2. Segunda prueba: discriminante igual a cero

Se utiliza la ecuación:

**x² − 4x + 4 = 0**

La solución es doble: `x = 2`.

```python
def test_solucion_doble():
    assert ecuacion2(1, -4, 4) == (2, 2)
```

**Error detectado:** inicialmente, el programa consideraba que un discriminante igual a cero no tenía solución y devolvía `None`.

![Error detectado con solución doble](<images/Captura de pantalla 2026-10-15 212834.png>)

**Corrección aplicada:**

```python
if discriminante == 0:
    x = -b / (2 * a)
    return (x, x)
```

Se añadió una condición específica para devolver la raíz doble.

### 4.3. Tercera prueba: soluciones decimales

Se comprueba la ecuación:

**2x² − 3x + 1 = 0**

Soluciones esperadas: `(1, 0.5)`.

```python
def test_soluciones_decimales():
    assert ecuacion2(2, -3, 1) == (1, 0.5)
```

**Error detectado:** el programa devolvía `(1, 0)` porque utilizaba `int()` para convertir las soluciones a enteros.

![Error con soluciones decimales](<images/Captura de pantalla 2026-10-15 213441.png>)

**Corrección aplicada:**

```python
return (x1, x2)
```

Se eliminó la conversión a enteros para conservar las soluciones decimales.

### 4.4. Cuarta prueba: coeficiente cuadrático igual a cero

Una ecuación de segundo grado requiere que el coeficiente `a` sea distinto de cero.

Se creó una prueba para comprobar que el programa rechaza este valor.

```python
import pytest

def test_coeficiente_cuadratico_cero():
    with pytest.raises(ValueError):
        ecuacion2(0, 2, 4)
```

**Error detectado:** el programa intentaba dividir entre cero y generaba `ZeroDivisionError`.

![Error de división entre cero](<images/Captura de pantalla 2026-10-15 213925.png>)

**Corrección aplicada:**

```python
if a == 0:
    raise ValueError("El coeficiente a no puede ser cero")
```

Se añadió una validación para controlar expresamente este caso.

### 4.5. Quinta prueba: sin soluciones reales

Se comprueba la ecuación:

**x² + 1 = 0**

El discriminante es negativo:

**Δ = −4**

```python
def test_sin_solucion_real():
    assert ecuacion2(1, 0, 1) is None
```

El programa informa de que no existen soluciones reales y devuelve `None`.

## 5. Refactorización

Después de conseguir que las pruebas pasaran, se simplificó la estructura condicional.

Inicialmente:

```python
elif discriminante > 0:
```

Se sustituyó por:

```python
else:
```

Como los casos de discriminante cero y negativo ya estaban contemplados, no era necesario comprobar nuevamente que fuese positivo.

Las pruebas automatizadas permitieron verificar que esta modificación no alteraba los resultados de los casos comprobados.

## 6. Resultado final

Después de corregir los errores y ejecutar nuevamente las pruebas, se obtuvo el siguiente resultado:

![Resultado final: cinco pruebas superadas](<images/Captura de pantalla 2026-10-15 214543.png>)

**Resultado: 5 passed in 0.16s**

| Prueba | Resultado |
|---|---|
| Dos soluciones reales | PASSED |
| Solución doble | PASSED |
| Sin soluciones reales | PASSED |
| Soluciones decimales | PASSED |
| Coeficiente cuadrático cero | PASSED |

## 7. Instalación y ejecución

### Crear un entorno virtual en Windows

```powershell
python -m venv venv
```

### Activar el entorno virtual

```powershell
.\venv\Scripts\Activate.ps1
```

### Instalar pytest

```powershell
python -m pip install pytest
```

### Ejecutar las pruebas

Desde la carpeta principal del proyecto:

```powershell
python -m pytest -v
```

El parámetro `-v` permite visualizar detalladamente el resultado de cada prueba.

## 8. Conclusiones

Mediante este proyecto he practicado:

- La organización de un proyecto Python en carpetas `src` y `test`.
- La creación y activación de entornos virtuales.
- La configuración y ejecución de pruebas con `pytest`.
- La utilización de `assert` para comparar resultados.
- La detección de errores mediante pruebas automatizadas.
- El manejo de excepciones con `raise` y `pytest.raises()`.
- La aplicación del ciclo RED → GREEN → REFACTOR.

El desarrollo mediante TDD ha permitido detectar problemas que inicialmente no estaban contemplados en la función, corregirlos y comprobar que las funcionalidades anteriores seguían funcionando.

## 9. Referencias

Repositorio de referencia del profesor:

https://github.com/dfleta/kata_tdd_pytest