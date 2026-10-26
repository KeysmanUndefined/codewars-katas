from .morse_code import MORSE_CODE


def decode_morse(morse_code):

    resultado = ""
    palabras = morse_code.strip().split("   ")

    for palabra in palabras:
        for letra in palabra.split(" "):
            codigo = MORSE_CODE[letra]
            resultado += codigo

        resultado += " "

    return resultado.strip()
