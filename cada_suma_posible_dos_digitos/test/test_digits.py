from src.digits import digits

def test_dos_digitos():
    assert digits(12) == [3]

def test_tres_digitos():
    assert digits(123) == [3, 4, 5]

def test_un_digito():
    assert digits(5) == []


def test_cero():
    assert digits(0) == []


def test_digitos_repetidos():
    assert digits(111) == [2, 2, 2]

def test_cinco_digitos():
    assert digits(12345) == [3, 4, 5, 6, 5, 6, 7, 7, 8, 9]