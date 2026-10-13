def alphabet_position(text):
    
    resultado = ""
    text = text.lower()

    for i in text:
        
        if "a" <= i <= "z":
            
            resultado = resultado + str(ord(i) -96) + " "
            
    resultado = resultado.strip()
            
            
            
    return resultado