def is_vow(inp):
    solucion = []
    for i in inp:
        if i == 101:
            i = "e"
            solucion.append(i)
        elif i == 117:
            i = "u"
            solucion.append(i)
        elif i == 97:
            i = "a"
            solucion.append(i)

        elif i == 105:
             i = "i"
             solucion.append(i)

        elif i == 111:
            i = "o"
            solucion.append(i)

        else:
            solucion.append(i)
                            

    return solucion      



if __name__ == "__main__":

    assert is_vow([118,117,120,121,117,98,122,97,120,106,104,116,113,114,113,120,106]) == [118,"u",120,121,"u",98,122,"a",120,106,104,116,113,114,113,120,106]

    assert is_vow([101,121,110,113,113,103,121,121,101,107,103]) == ["e",121,110,113,113,103,121,121,"e",107,103]

    assert is_vow([118,103,110,109,104,106]) == [118,103,110,109,104,106]

    assert is_vow([107,99,110,107,118,106,112,102]) == [107,99,110,107,118,106,112,102]

    assert is_vow([100,100,116,105,117,121]) == [100,100,116,"i","u",121]

    print("Todos los tests superados")