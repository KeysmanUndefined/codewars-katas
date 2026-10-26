# Testing - Decode the Morse Code (6 kyu)

## Objetivo

Comprobar mediante pruebas automatizadas que la función `decode_morse()` traduce correctamente mensajes escritos en código Morse.

Para realizar las pruebas he utilizado **pytest**.

## Pruebas realizadas

| Test | Descripción | Resultado |
|---|---|---|
| `test_una_letra` | Traducción de una única letra Morse | PASSED |
| `test_una_palabra` | Traducción de una palabra completa | PASSED |
| `test_dos_palabras` | Traducción de dos palabras separadas por tres espacios | PASSED |
| `test_espacios_exteriores` | Eliminación de espacios al principio y al final | PASSED |
| `test_mensaje_codewars` | Traducción del ejemplo HEY JUDE | PASSED |
| `test_sos` | Traducción de la secuencia especial SOS | PASSED |

## Ejecución de las pruebas

Desde la raíz del repositorio:

```bash
python -m pytest decode_morse/tests/ -v
```

## Resultados

**6 pruebas superadas.**

Las pruebas comprueban tanto la traducción de letras individuales como de palabras y mensajes completos.

También verifican el tratamiento de espacios adicionales mediante `strip()`.

## Conclusión

La función supera los seis casos de prueba definidos.

Este ejercicio me ha permitido practicar:

- El uso de `split()` y `strip()`.
- Los bucles `for` anidados.
- El acceso a valores de un diccionario.
- La construcción de cadenas mediante concatenación.
- La creación y ejecución de pruebas automatizadas con pytest.

La solución mantiene la estructura original desarrollada para Codewars.