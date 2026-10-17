
# Duplicate Encoder

Ejercicio de Python basado en el kata [Duplicate Encoder](https://www.codewars.com/kata/54b42f9314d9229fd6000d9c) de Codewars (6 kyu).

## Enunciado

Crear una función que transforme una cadena de texto:

- `(` si el carácter aparece una sola vez.
- `)` si el carácter aparece más de una vez.

La comparación no distingue entre mayúsculas y minúsculas.

## Ejemplos

| Entrada | Resultado |
|---|---|
| `"din"` | `"((("` |
| `"recede"` | `"()()()"` |
| `"Success"` | `")())())"` |
| `"(( @"` | `"))(("` |

## Mi solución

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

## Cómo funciona

1. Inicializamos una cadena vacía para guardar el resultado.
2. Convertimos el texto a minúsculas con `.lower()`.
3. Recorremos cada carácter mediante un bucle `for`.
4. Utilizamos `.count()` para comprobar cuántas veces aparece.
5. Añadimos `(` o `)` según corresponda.
6. Devolvemos la cadena resultante con `return`.

## Pruebas automatizadas

El proyecto incluye cuatro pruebas con `pytest`, todas superadas.

Para ejecutarlas desde la carpeta `Duplicate_Encoder`:

```powershell
python -m pytest -v
```

Consulta [TESTING.md](TESTING.md) para ver las pruebas, los resultados y las capturas de pantalla.

## Archivos del proyecto

- `duplicate_encoder.ipynb`: explicación detallada en Jupyter.
- `src/duplicate_encoder.py`: implementación de la función.
- `test/test_duplicate_encoder.py`: pruebas automatizadas.
- `pytest.ini`: configuración de pytest.
- `TESTING.md`: documentación de las pruebas.
- `images/`: capturas de pantalla.

## Autor

[KeysmanUndefined](https://github.com/KeysmanUndefined) · [Repositorio Codewars Katas](https://github.com/KeysmanUndefined/codewars-katas)
