def revolver(veces): # crea la funcion 
    # Crea una baraja de 40 cartas
    baraja = [
        "o1","o2","o3","o4","o5","o6","o7","o8","o9","o10",
        "e1","e2","e3","e4","e5","e6","e7","e8","e9","e10",
        "b1","b2","b3","b4","b5","b6","b7","b8","b9","b10",
        "c1","c2","c3","c4","c5","c6","c7","c8","c9","c10"
        ]
    c = 0 # variable contadora
    # mientras el contador sea menor a las veces que se tienen que mezclar
    while c < veces: 
        # divide la baraja en dos arreglos de 20
        mitad = len(baraja) // 2
        arreglo1 = baraja[:mitad]
        arreglo2 = baraja[mitad:]

        
        array3 = [] # arreglo para guardar las cartas

        # mientras arreglo1 y arreglo2 tengan elementos 
        while arreglo1 and arreglo2:
            # selecciona el primer elemento y lo borra
            carta_arreglo1 = arreglo1.pop(0)
            # selecciona el ultimo elemento y lo borra
            carta_arreglo2 = arreglo2.pop()
            # agrega el primer elemento al arreglo3
            array3.append(carta_arreglo1)
            # agrega el ultimo elemento al arreglo3
            array3.append(carta_arreglo2)
        c += 1 # contador incrementa 1
        baraja = array3 # la baraja completa ahora es igual al array3
    return baraja # devuelve la baraja completa

# Pide al usuario cuántas veces desea realizar el proceso
veces = int(input("¿Cuántas veces deseas revolver la baraja? "))
resultado= revolver(veces)
print(resultado)
