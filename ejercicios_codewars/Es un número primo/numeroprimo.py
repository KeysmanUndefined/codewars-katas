def is_prime(num):
    
    import math

    # Verifico si el número es menor o igual a 1, en cuyo caso no es primo y haria return false.  Esto es importante para que no se ejecute el for y no de error al intentar calcular la raiz cuadrada de un numero negativo.  La raiz cuadrada de un numero negativo no existe en los numeros reales, por lo que daria error.
    
    if (num <=1):
            return False


    # Para encontrar numeros primos, se debe verificar si el número es divisible por algún número entre 2 y la raíz cuadrada del número. 
    # Sumo uno a la raiz cuadrada por si el numero es 9. math.sqrt(9) = 3.0.  La suma +1 int(3.0) = 3.  3 + 1 = 4.  Debe quedar fuera del int pues primero quiero encontrar la raiz cuadrada y luego convertirla a entero para poder sumar 1 despues
    
    for numero in range(2,(int(math.sqrt(num))+1)):
        
        
        
        if (num%numero==0):
            return False 
                        
                      
                    
                      

    else:
            
        return True

print(is_prime(7))