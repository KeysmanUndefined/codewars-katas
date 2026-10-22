def digits(n):
    
    n = str(n)
    resultado=[]
    
    for i in range(len(n)):
        
        for j in range(i + 1,len(n)):
            
            resultado.append(int(n[i]) + int(n[j]))
            
    
    return resultado