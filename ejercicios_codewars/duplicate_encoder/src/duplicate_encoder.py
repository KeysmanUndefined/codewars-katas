def duplicate_encode(word):
    
    code = ""    
    word = word.lower()
    
    for letra in word:        
        if word.count(letra) > 1:            
            code = code + ")"
        
        else:            
            code = code + "("
            
    return code