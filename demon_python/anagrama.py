def anagrama(cadena1, cadena2): # crea una funcion con dos parametros
    lista1 = list(cadena1) # pasa la cadena1 a una lista
    lista2 = list(cadena2) # pasa la cadena2 a otra lista
    for i in range(len(lista1)): # toma elemento por elemento de la lista1
        posicion = lista2.index(lista1[i]) # verifica si la letra actual esta en a  lista2
        
        if posicion != -1: # si la posicion no es igual a -1, es decir existe
            lista2.pop(posicion) # borra la letra de lista2 en dicha posicion
    if len(lista2) == 0: # al final del ciclo for verifica si la lista2 ha quedado vacia
        return "son anagramas" # positivo
    elif len(lista2) != 0: # verifica si la lista2 aun tiene elementos
        return "no son anagramas" # negativo
    
cadena1 = input("Escribe la cadena 1: ") # pide que se ingrese una cadena
cadena2 = input("Escribe la cadena 2: ") # pide que se ingrese otra cadena
print(anagrama(cadena1, cadena2)) # imprime y llama a la función
