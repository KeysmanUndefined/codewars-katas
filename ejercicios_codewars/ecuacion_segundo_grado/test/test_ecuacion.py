from src.ecuacion import ecuacion2


def test_dos_soluciones():
    assert ecuacion2(1, -5, 6) == (3, 2)

def test_solucion_doble():
    assert ecuacion2(1, -4, 4) == (2, 2)

def test_sin_solucion_real():
    assert ecuacion2(1, 0, 1) is None

def test_soluciones_decimales():
    assert ecuacion2(2, -3, 1) == (1, 0.5)

import pytest

def test_coeficiente_cuadratico_cero():
    with pytest.raises(ValueError):
        ecuacion2(0, 2, 4)