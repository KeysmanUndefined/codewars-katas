def multiTable(n: Int): String = 
    
        {var texto =  ""
 
    for (elemento <- 1 to 10){
         
        var resultado = elemento * n
          
    if (elemento == 10)
         
        {texto = texto + s"$elemento * $n = $resultado"}
         
    else {
        texto = texto + s"$elemento * $n = $resultado\n"}
 
}
         return texto
         }
