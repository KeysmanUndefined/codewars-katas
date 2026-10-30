# Pruebas automáticas — Duplicate Encoder

## Objetivo

Comprobar el funcionamiento de la función `duplicate_encode()` mediante pruebas automáticas con **pytest**, separando el código fuente de los casos de prueba. Se documenta también un fallo provocado intencionadamente para aprender a interpretar los mensajes de error.

## Estructura del proyecto

```text
Duplicate_Encoder/
├── images/
│   ├── Captura de pantalla 2026-10-17 205052.png
│   ├── Captura de pantalla 2026-10-17 205222.png
│   ├── Captura de pantalla 2026-10-17 205321.png
│   ├── Captura de pantalla 2026-10-17 205443.png
│   └── Captura de pantalla 2026-10-17 205604.png
├── src/
│   ├── __init__.py
│   └── duplicate_encoder.py
├── test/
│   ├── __init__.py
│   └── test_duplicate_encoder.py
├── duplicate_encoder.ipynb
├── pytest.ini
├── README.md
└── TESTING.md
```

## Preparación e instalación

Desde la terminal de VS Code, accedemos al directorio del ejercicio. Por ejemplo, si estamos en la carpeta que contiene `codewars-katas`:

```powershell
cd codewars-katas
cd Duplicate_Encoder
```

Comprobamos que estamos en el directorio correcto:

```powershell
pwd
```

Instalamos pytest en el intérprete de Python utilizado:

```powershell
python -m pip install pytest
```

Comprobamos la instalación:

```powershell
python -m pytest --version
```

En las capturas se utilizó **Python 3.13.3** y **pytest 9.1.1** en Windows.

## Configuración de pytest

Creamos `pytest.ini` en la raíz del ejercicio:

```ini
[pytest]
testpaths = test
pythonpath = .
```

- `testpaths = test` indica la carpeta donde pytest buscará las pruebas.
- `pythonpath = .` añade la raíz del proyecto a la ruta de importación.

## Código que vamos a probar

Archivo `src/duplicate_encoder.py`:

```python
def duplicate_encode(word):
    code = ""
    word = word.lower()

    for letra in word:
        if word.count(letra) > 1:
            code = code + ")"
        else:
            code = code + "("

    return code
```

El ejercicio pide representar cada carácter mediante `"("` cuando aparece una sola vez y mediante `")"` cuando aparece más de una vez, sin distinguir entre mayúsculas y minúsculas.

## Creación de los casos de prueba

Archivo `test/test_duplicate_encoder.py`:

```python
from src.duplicate_encoder import duplicate_encode


def test_din():
    assert duplicate_encode("din") == "((("


def test_recede():
    assert duplicate_encode("recede") == "()()()"


def test_success():
    assert duplicate_encode("Success") == ")())())"


def test_caracteres_especiales():
    assert duplicate_encode("(( @") == "))(("
```

Cada función empieza por `test_` para que pytest la detecte. La instrucción `assert` comprueba que el valor devuelto por la función coincide con el esperado.

## Ejecución

Desde la carpeta `Duplicate_Encoder` ejecutamos:

```powershell
python -m pytest -v
```

La opción `-v` muestra los nombres y resultados de las pruebas.

## Evidencias de ejecución

### 1. Primer caso: caracteres no repetidos

Probamos `"din"`, que debe producir `"((("`. Se ejecuta correctamente una prueba.

![Primer test superado](<images/Captura de pantalla 2026-10-17 205052.png>)

### 2. Segundo caso: caracteres repetidos

Añadimos `"recede"`, que debe producir `"()()()"`. Las dos pruebas pasan.

![Dos tests superados: 2 passed](<images/Captura de pantalla 2026-10-17 205222.png>)

### 3. Tercer caso: mayúsculas y minúsculas

Añadimos `"Success"`, que debe producir `")())())"`. Comprobamos que `.lower()` permite tratar `S` y `s` como el mismo carácter.

![Tres tests superados: 3 passed](<images/Captura de pantalla 2026-10-17 205321.png>)

### 4. Fallo provocado intencionadamente

Para entender los mensajes de error, añadimos temporalmente un test con un resultado esperado incorrecto:

```python
def test_error_intencionado():
    assert duplicate_encode("din") == ")))"
```

La función devuelve `"((("`, no `")))"`. Por tanto, pytest muestra `FAILED`, un `AssertionError` y el resumen **1 failed, 3 passed**. El fallo demuestra que la prueba detecta una discrepancia; no significa que la función esté mal implementada.

![Error intencionado: 1 failed, 3 passed](<images/Captura de pantalla 2026-10-17 205443.png>)

Después **eliminamos el test incorrecto**; no debe permanecer en la versión final.

### 5. Cuarto caso: símbolos y espacios

Añadimos la entrada `"(( @"`: los dos paréntesis de apertura originales están repetidos, mientras que el espacio y `@` aparecen una sola vez. El resultado esperado son **dos `)` seguidos de dos `(`**, como se indica en el test.

Las cuatro pruebas pasan en la ejecución final.

![Resultado final: 4 passed](<images/Captura de pantalla 2026-10-17 205604.png>)
## Interpretación de los resultados

| Mensaje | Significado |
|---|---|
| `PASSED` | El test se ha superado |
| `FAILED` | El test no ha cumplido la condición comprobada |
| `AssertionError` | Una afirmación realizada mediante `assert` es falsa |
| `4 passed` | Los cuatro casos definidos han pasado |

## Conclusión

Se han creado cuatro casos de prueba automáticos y se ha comprobado que la función devuelve los resultados esperados para las entradas utilizadas. También se ha provocado un fallo para aprender a interpretar la información que ofrece pytest.

**Resultado final documentado: 4 passed.** Esto no garantiza que todas las entradas posibles estén cubiertas; en el futuro se pueden añadir pruebas para cadenas vacías y otros casos límite.

## Referencias

- [Kata Duplicate Encoder — Codewars](https://www.codewars.com/kata/54b42f9314d9229fd6000d9c)
- [Documentación de pytest](https://docs.pytest.org/)
