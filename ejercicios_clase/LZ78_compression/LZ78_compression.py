def encoder(data):
    diccionario = {0:""}
    codigo = ""
    cadena = ""
    for i in data:
        cadena += i

        if cadena not in diccionario.values():
            diccionario[len(diccionario)] = cadena




def test_encoder():
    assert encoder("ABAABABAABAB") == "0A0B1A2A4A4B"
    print("TEST SUPERADO")


test_encoder()