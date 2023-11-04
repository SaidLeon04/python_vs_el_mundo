def palindromo(cadena): # crea una funcion con un parametro 
    lista = list(cadena) # pasa la cadena a una lista
    lista2 = [] # crea una segunda lista
    longitud = len(lista) # obtiene la longitud de la lista con la cadena
    i = 0 # iterador iniciando en 0

    while i < longitud: # mientras el iterador sea menor que la longitud
        lista2.append(lista[i]) # añade letra por letra a la segunda lista
        i += 1 # iterador incrementa uno 
    cadena2 = lista2[::-1] # voltea todos los elementos en la lista dos
    cadena3 = ''.join(cadena2) # convierta la lista volteada a un string
    if cadena == cadena3: # compara si ambos strings son iguales
        return "es un palindromo" # positivo
    elif cadena != cadena3: # compara si ambos strings no son iguales
        return "no es un palindromo" # negativo

cadena = input("Escribe una cadena: ") # pide que se escriba una cadena
print(palindromo(cadena)) # llama e imprime el resultado de la funcion
