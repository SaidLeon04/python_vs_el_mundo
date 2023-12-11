def adivinacion(array1, array2, array3, paises): # define la funcion adivinacion
    k = 3 # variable para revolver 3 veces
    while k > 0: # mientras k sea mayor a 0
        array1 = [] # array 1 vacio
        array2 = [] # array 2 vacio
        array3 = [] # array 3 vacio

        for i, pais in enumerate(paises): # para i y pais en la lista de paises
            if i % 3 == 0: # si el residuo de i entre 3 es 0
                array1.append(pais) # agrega el pais al array 1
            elif i % 3 == 1: # si el residuo de i entre 3 es 1
                array2.append(pais) # agrega el pais al array 2
            else: # caso contrario
                array3.append(pais) # agrega el pais al array 3
            
        paises = [] # vacia paises
        print("Lista 1: ", array1) # imprime el array 1
        print("Lista 2: ", array2) # imprime el array 2
        print("Lista 3: ", array3) # imprime el array 3
        pos = input("En que lista se encuentra el pais? (1, 2 o 3): ") # pregunta en que lista se encuentra el pais
        if(pos == "1"): # si la respuesta es 1
            paises = array2 + array1 + array3 # integra los paises en ese orden
        elif(pos == "2"): # si la respuesta es 2
            paises = array1 + array2 + array3 # integra los paises en ese orden
        elif(pos == "3"): # si la respuesta es 3
            paises = array1 + array3 + array2 # integra los paises en ese orden
        k -= 1 # decrementa k en 1
    return paises[10] # regresa el pais en la posicion 10 de la lista paises cuando while no se cumple

# array de paises 
paises = [
    "Estados Unidos", "Canada", "Mexico", "Brasil", "Argentina",
    "Reino Unido", "Francia", "Alemania", "Italia", "España",
    "China", "Japón", "Corea del Sur", "India", "Australia",
    "Rusia", "Sudáfrica", "Egipto", "Turquía", "Arabia Saudita",
    "Nigeria"
]
print(paises) # imprime la lista de paises
print("Piensa en un pais de los anteriores... ") # instrucciones
array1 = []
array2 = []
array3 = []
print(adivinacion(array1, array2, array3, paises)) # llamada a la funcion

