from decode_morse.src.decode_morse import decode_morse


def test_una_letra():
    assert decode_morse("....") == "H"


def test_una_palabra():
    assert decode_morse(".... --- .-.. .-") == "HOLA"


def test_dos_palabras():
    assert decode_morse(".... --- .-.. .-   -- ..- -. -.. ---") == "HOLA MUNDO"


def test_espacios_exteriores():
    assert decode_morse("   .... --- .-.. .-   ") == "HOLA"


def test_mensaje_codewars():
    assert decode_morse(".... . -.--   .--- ..- -.. .") == "HEY JUDE"


def test_sos():
    assert decode_morse("...---...") == "SOS"
