def permute_a_palindrome(input):
    impares = 0
    contador = 0

    # set() crea un conjunto con las letras diferentes de la palabra, eliminando los duplicados.
    for letra in set(input):
        # .count() cuenta cada vez que aparece un elemento. Letra en este caso
        contador = input.count(letra)
        if contador % 2 != 0:
            impares += 1

    if impares <= 1:
        return True
    else:
        return False