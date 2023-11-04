import random # importa la libreria random para generar numeros aleatorios

# funcion para jugar contra CPU
def juego_cpu(matrix, ocupados, jugada, turno, jugador, cpu):
    while True: # ciclo para repetir las jugadas
        while jugada < 9: # ciclo para contar las jugadas
            if turno == 1: # si el turno random le correspondio al jugador1
                # pide la entrada de un numero que representara la posicion
                posicion = int(input("Escribe la posicion de tu jugada: "))
                if posicion not in ocupados: # comprueba que la posicion no este ocupada
                    ocupados.append(posicion) # agrega la posicion a las ya ocupadas
                    jugada += 1 # jugada incrementa mas 1
                    turno = 2 # el turno pasa el cpu
                    # varios IF para controlar en que posicion poner la marca del jugador actual                    
                    if posicion == 1: # si posicion es igual a 1
                        matrix[0][0] = jugador # una marca del jugador se colocara en la posicion 0,0 de la matriz
                    elif posicion == 2:
                        matrix[0][1] = jugador
                    elif posicion == 3:
                        matrix[0][2] = jugador
                    elif posicion == 4:
                        matrix[1][0] = jugador
                    elif posicion == 5:
                        matrix[1][1] = jugador
                    elif posicion == 6:
                        matrix[1][2] = jugador
                    elif posicion == 7:
                        matrix[2][0] = jugador
                    elif posicion == 8:
                        matrix[2][1] = jugador
                    elif posicion == 9: # si posicion es igual a 1
                        matrix[2][2] = jugador # una marca del jugador se colocara en la posicion 2,2 de la matriz

                    # comprueba si hay ganador despues de la jugada 5
                    if jugada >= 5:
                       comprobarJ1(matrix, jugador) # llama a la funcion comprobarJ1 para verificar si el jugador1 ha ganado
                else: # caso contrario de que la posicion si este ocupada previamente
                    print("Posicion ocupada, juega de nuevo") # imprime una advertencia y se repetira la jugada
                    print(ocupados) # imprime las posiciones ya ocupadas

            elif turno == 2: # si el turno random le correspondio al cpu
                print("Juega CPU: ") # indica que es el turno de cpu
                posicion = random.randint(1, 9) # genera un numero aleatorio para la posicion que cpu colocará
                if posicion not in ocupados: # comprueba que la posición no este ocupada
                    ocupados.append(posicion) # agrega la posición a las ya ocupadas
                    jugada += 1 # jugada incrementa mas 1
                    turno = 1 # pasa el turno al siguiente jugador
                    print("CPU jugó en la posicion: ", posicion) # indica la posición en la que ha jugado cpu
                    # varios IF para controlar en que posicion poner la marca del jugador actual         
                    if posicion == 1: 
                        matrix[0][0] = cpu
                    elif posicion == 2:
                        matrix[0][1] = cpu
                    elif posicion == 3: # si posicion es igual a 3
                        matrix[0][2] = cpu # una marca del jugador se colocara en la posicion 0,2 de la matriz
                    elif posicion == 4:
                        matrix[1][0] = cpu
                    elif posicion == 5:
                        matrix[1][1] = cpu
                    elif posicion == 6: # si posicion es igual a 6
                        matrix[1][2] = cpu # una marca del jugador se colocara en la posicion 1,2 de la matriz
                    elif posicion == 7:
                        matrix[2][0] = cpu
                    elif posicion == 8:
                        matrix[2][1] = cpu
                    elif posicion == 9:
                        matrix[2][2] = cpu
                    # comprueba si hay ganador despues de la jugada 5
                    if jugada >= 5:
                        comprobarCPU(matrix, cpu) # llama a la función correspondiente para comprobar si ha ganado cpu
                else: # caso contrario en que la posición si este ocupada previamente 
                    print("Posicion ocupada, juega de nuevo") # imprime una advertencia
                    print(ocupados) # imprime las posiciones ya ocupadas
            break # rompe los ciclos while, el juego termino

# funcion para jugar contra otro jugador
def juego_jugadores(matrix, ocupados, jugada, turno, jugador1, jugador2):
    while True: # ciclo para repetir las jugadas
        while jugada < 9: # ciclo para contar las jugadas
            if turno == 1: # si el turno random le correspondio al jugador1
                # pide la entrada de un numero que representara la posicion
                posicion = int(input("Jugador 1\nescribe la posicion de tu jugada: ")) 
                if posicion not in ocupados: # comprueba que la posición no este ocupada
                    ocupados.append(posicion) # agrega la posición a las ya ocupadas
                    jugada += 1 # jugada incrementa mas 1
                    turno = 2 # pasa el turno al siguiente jugador
                    # varios IF para controlar en que posicion poner la marca del jugador actual       
                    if posicion == 1:
                        matrix[0][0] = jugador1
                    elif posicion == 2:
                        matrix[0][1] = jugador1
                    elif posicion == 3:
                        matrix[0][2] = jugador1
                    elif posicion == 4:
                        matrix[1][0] = jugador1
                    elif posicion == 5: # si posicion es igual a 5
                        matrix[1][1] = jugador1 # una marca del jugador se colocara en la posicion 1,1 de la matriz
                    elif posicion == 6:
                        matrix[1][2] = jugador1
                    elif posicion == 7:
                        matrix[2][0] = jugador1
                    elif posicion == 8: # si posicion es igual a 8
                        matrix[2][1] = jugador1 # una marca del jugador se colocara en la posicion 2,1 de la matriz
                    elif posicion == 9:
                        matrix[2][2] = jugador1
                    # comprueba si hay ganador despues de la jugada 5
                    if jugada >= 5:
                        comprobarJ1(matrix, jugador1) # llama a la función correspondiente para comprobar si ha ganado jugador1
                else:
                    print("Posicion ocupada, juega de nuevo") # imprime una advertencia
                    print(ocupados) # imprime las posiciones ya ocupadas

            elif turno == 2: # si el turno random le correspondio al jugador2
                # pide la entrada de un numero que representara la posicion
                posicion = int(input("Jugador 2\nEscribe la posicion de tu jugada: "))
                if posicion not in ocupados: # comprueba que la posición no este ocupada
                    ocupados.append(posicion) # agrega la posición a las ya ocupadas
                    jugada += 1 # jugada incrementa mas 1
                    turno = 1 # pasa el turno al siguiente jugador
                    # varios IF para controlar en que posicion poner la marca del jugador actual       
                    if posicion == 1:
                        matrix[0][0] = jugador2
                    elif posicion == 2:
                        matrix[0][1] = jugador2
                    elif posicion == 3:
                        matrix[0][2] = jugador2
                    elif posicion == 4:
                        matrix[1][0] = jugador2
                    elif posicion == 5:
                        matrix[1][1] = jugador2
                    elif posicion == 6:
                        matrix[1][2] = jugador2
                    elif posicion == 7: # si posicion es igual a 7
                        matrix[2][0] = jugador2 # una marca del jugador se colocara en la posicion 2,0 de la matriz
                    elif posicion == 8:
                        matrix[2][1] = jugador2
                    elif posicion == 9:
                        matrix[2][2] = jugador2
                    # comprueba si hay ganador despues de la jugada 5
                    if jugada >= 5:
                        comprobarJ2(matrix, jugador2)  # llama a la función correspondiente para comprobar si ha ganado jugador2
                else:
                    print("Posicion ocupada, juega de nuevo") # imprime una advertencia
                    print(ocupados) # imprime las posiciones ya ocupadas
            break

# funcion para comprobar si el jugador1 ha ganado
def comprobarJ1(matrix, jugador1):
    for fila in matrix: # ciclo for para recorrer toda la matriz por filas
        repeticiones = fila.count(jugador1) # cuenta las veces que aparece la marca de jugador1 en una fila
        if repeticiones == 3: # si apareció 3 veces
            print("Jugador 1 ha ganado!!") # imprime al ganador
            for fila in matrix: # recorre toda la matriz 
                print(fila) # imprime la matriz con el resultado final
            print("Gracias por jugar... ")
            exit() # sale del programa

    # comprueba si hay ganador en las columnas
    for columna in range(3): # ciclo for para recorrer toda la matriz por columnas
        repeticiones = 0 # variable igual a 0
        for fila in matrix: # recorre toda la matriz
            # comprueba si un elemento de una columna es igual a la marca de jugador1
            if fila[columna] == jugador1:
                repeticiones += 1 # repeticiones incrementa mas 1
                if repeticiones == 3: # si hay 3 repeticiones
                    print("Jugador 1 ha ganado!!") # imprime al ganador
                    for fila in matrix: # recorre toda la matriz 
                        print(fila) # imprime la matriz con el resultado final
                    print("Gracias por jugar... ")
                    exit() # sale del programa
    # comprueba si hay ganador en las diagonales
    # recorre la matriz y devuelve true si hay 3 marcas iguales
    diagonal_1 = all(matrix[i][i] == matrix[0][0] for i in range(3))
    # recorre la matriz y devuelve true si hay 3 marcas iguales
    diagonal_2 = all(matrix[i][3 - 1 - i] == matrix[0][3 - 1] for i in range(3))
    # si cualquiera de las diagonales es verdadera
    if diagonal_1 or diagonal_2:
        print("Jugador 1 ha ganado!!") # imprime al ganador
        for fila in matrix: # recorre toda la matriz 
            print(fila) # imprime la matriz con el resultado final
        print("Gracias por jugar... ") 
        exit() # sale del programa

# funcion para comprobar si el jugador2 ha ganado
def comprobarJ2(matrix, jugador2):
    for fila in matrix:  # ciclo for para recorrer toda la matriz por filas
        repeticiones = fila.count(jugador2) # cuenta las veces que aparece la marca de jugador2 en una fila
        if repeticiones == 3: # si apareció 3 veces
            print("Jugador 2 ha ganado!!") # imprime al ganador
            for fila in matrix: # recorre toda la matriz 
                print(fila) # imprime la matriz con el resultado final
            exit() # sale del programa
    # comprueba si hay ganador en las columnas
    for columna in range(3): # ciclo for para recorrer toda la matriz por columnas
        repeticiones = 0 # variable para contar las repeticiones
        for fila in matrix: # recorre toda la matriz
            if fila[columna] == jugador2: # comprueba si un elemento de una columna es igual a la marca de jugador2
                repeticiones += 1 # repeticiones incrementa mas 1
                if repeticiones == 3: # si hay 3 repeticiones
                    print("Jugador 2 ha ganado!!") # imprime al ganador
                    for fila in matrix: # recorre toda la matriz
                        print(fila) # imprime la matriz con el resultado final
                    exit() 
    # comprueba si hay ganador en las diagonales
    # recorre la matriz y devuelve true si hay 3 marcas iguales  
    diagonal_1 = all(matrix[i][i] == matrix[0][0] for i in range(3))
    # recorre la matriz y devuelve true si hay 3 marcas iguales
    diagonal_2 = all(matrix[i][3 - 1 - i] == matrix[0][3 - 1] for i in range(3))
    # si cualquiera de las diagonales es verdadera
    if diagonal_1 or diagonal_2:
        print("Jugador 2 ha ganado!!") # imprime al ganador
        for fila in matrix: # recorre toda la matriz
            print(fila) # imprime la matriz con el resultado final
        exit() 
# funcion para comprobar si el cpu ha ganado
def comprobarCPU(matrix, cpu):

    for fila in matrix: # ciclo for para recorrer toda la matriz por filas
        repeticiones = fila.count(cpu) # cuenta las veces que aparece la marca de cpu en una fila
        if repeticiones == 3: # si apareció 3 veces
            print("CPU ha ganado!!") # imprime al ganador
            for fila in matrix: # recorre toda la matriz 
                print(fila) # imprime la matriz con el resultado final
            exit() # sale del programa
    # comprueba si hay ganador en las columnas
    for columna in range(3): # ciclo for para recorrer toda la matriz por columnas
        repeticiones = 0 # variable para contar las repeticiones
        for fila in matrix: # recorre toda la matriz
            if fila[columna] == cpu: # comprueba si un elemento de una columna es igual a la marca de cpu
                repeticiones += 1 # repeticiones incrementa mas 1
                if repeticiones == 3: # si hay 3 repeticiones
                    print("CPU ha ganado!!") # imprime al ganador
                    for fila in matrix: # recorre toda la matriz
                        print(fila) # imprime la matriz con el resultado final
                    exit()
    # comprueba si hay ganador en las diagonales
    # recorre la matriz y devuelve true si hay 3 marcas iguales  
    diagonal_1 = all(matrix[i][i] == matrix[0][0] for i in range(3))
    # recorre la matriz y devuelve true si hay 3 marcas iguales
    diagonal_2 = all(matrix[i][3 - 1 - i] == matrix[0][3 - 1] for i in range(3))
    # si cualquiera de las diagonales es verdadera
    if diagonal_1 or diagonal_2:
        print("Jugador 1 ha ganado!!") # imprime al ganador
        for fila in matrix: # recorre toda la matriz
            print(fila) # imprime la matriz con el resultado final
        exit() 

# funcion para iniciar el juego
def gato(jugadores): 
    if jugadores == 1: # si la opcion del menú fue igual a 1
        ocupados = [] # array para almacenar las posiciones ocupadas
        # tablero del juego representado en una matriz 3x3
        matrix = [ 
            ['1','2','3'],
            ['4','5','6'],
            ['7','8','9']
        ]
        jugada = 0 # variable para contar las jugadas
        turno = random.randint(1, 2) # numero aleatorio para determinar los turnos
        personaje = input("Jugador, elige tu personaje: X o O: ") # variable para determinar la marca de cada jugador
        # ciclo if para asignar la marca a cada jugador e iniciar la partida     
        if personaje == "X":
            jugador1 = "X"
            jugador2 = "O"
            juego_jugadores(matrix, ocupados, jugada, turno, jugador1, jugador2)
        elif personaje == "O":
            jugador1 = "O"
            jugador2 = "X"
            juego_jugadores(matrix, ocupados, jugada, turno, jugador1, jugador2)
        else: # caso contrario 
            print("Ese personaje no existe, por ahora...") 
    
    if jugadores == 2: # si la opcion del menú fue igual a 2
        ocupados = [] # array para almacenar las posiciones ocupadas
        # tablero del juego representado en una matriz 3x3
        matrix = [
            ['1','2','3'],
            ['4','5','6'],
            ['7','8','9']
        ]
        jugada = 0 # variable para contar las jugadas
        turno = random.randint(1, 2) # numero aleatorio para determinar los turnos
        personaje = input("Elige tu personaje: X o O: ") # variable para determinar la marca de cada jugador
        # ciclo if para asignar la marca a cada jugador e iniciar la partida
        if personaje == "X":
            jugador = "X"
            cpu = "O"
            juego_cpu(matrix, ocupados, jugada, turno, jugador, cpu)

        elif personaje == "O":
            jugador = "O"
            cpu = "X"
            juego_cpu(matrix, ocupados, jugada, turno, jugador, cpu)
        
        else: # caso contrario
            print("Ese personaje no existe, por ahora...")
                
    if jugadores == 3: # si la opcion del menú fue igual a 2
        # instrucciones del juego        
        print("Presentando el tablero del juego:")
        for fila in matrix_tutorial:
            print(fila)
        matrix_tutorial = [['1','2','3'],
                        ['4','5','6'],
                        ['7','8','9']]
        print("Escribe el número de la posición que deseas jugar en el tablero")
    # salida
    if jugadores == 4:
        print("Gracias por jugar")
        exit()
    # caso contrario 
    else:
        print("Opción no valida")

# menú principal del juego
print("Gato \n 1. 1 vs 1 \n 2. 1 vs CPU \n 3. Tutorial\n 4. Salir")
# pide una opción al usuario
jugadores = int(input("Escribe una opción: "))
# llama a la funcion principal para iniciar el juego
gato(jugadores)
