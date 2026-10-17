from src.duplicate_encoder import duplicate_encode


def test_din():
    assert duplicate_encode("din") == "((("

def test_recede():
    assert duplicate_encode("recede") == "()()()"

def test_success():
    assert duplicate_encode("Success") == ")())())"

def test_caracteres_especiales():
    assert duplicate_encode("(( @") == "))(("