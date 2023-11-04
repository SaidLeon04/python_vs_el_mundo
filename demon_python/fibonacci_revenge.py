def fibonacci(n, a, b): # declaración de la función que utlizara 3 valores
    if n <= 0: # si n es menor o igual a 0 devolvera el array 
        return [] # retorna el array vacio
    elif n == 1: # si n es igual a 1 devvolvera el array con el valor de a
        return [a] # retorna el array con el valor de a
    elif n == 2: # si n es igual a 2 devvolvera el array con el valor de a y b
        return [a, b] # devuelve el array con los dos primeros digitos de la secuencia, 1 y 0
    else: # caso contrario a los anteriores
        # decrementa n menos 1 hasta llegar a 0
        # inicializa otra vez la función fibonacci con n disminuido, 
        # a con el valor actual de b, y b con el valor de a + b
        secuencia = fibonacci(n - 1, b, a + b)
        secuencia.insert(0, a) # Inserta el valor de a al principio del array
        return secuencia # retorna la secuencia 

n = 16 # numero de valores de la secuencia que se obtendran
#array para guardar los numeros de la secuencia, inicializado con los valores de la funcion
array = fibonacci(n, 0, 1)
print(array) # imprime el array
