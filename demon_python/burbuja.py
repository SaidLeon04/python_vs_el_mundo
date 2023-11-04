array = [12,2,33,55,8,98,4,32,32,12,89,0] # declaracion del arreglo
print(f"Arreglo desoordenado: ",array) # imprime el arreglo desordenado
n = len(array)
print(n) # longitud del arreglo almacenada en n
for i in range(n - 1): # ciclo for para recorrer el arreglo 11 veces
    for j in range(0, n - i - 1): # ciclo for para recorrer el arreglo 10 veces y comparar los valores

        if array[j] > array[j + 1]: # compara el valor en el indice j mayor que el siguiente valor
            # si la condición se cumple, se intercambian los valores de posición
            array[j], array[j + 1] = array[j + 1], array[j] 

print(f"Arreglo ordenado: ", array) # imprime el arreglo ordenado
