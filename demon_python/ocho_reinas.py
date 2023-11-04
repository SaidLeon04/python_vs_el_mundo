# Define una función llamada "tablero" que toma la cantidad de reinas como argumento
def tablero(reinas):
    # Inicializa un contador para llevar el registro de cuántas reinas se han colocado
    cont = 0

    # Mientras no se hayan colocado todas las reinas
    while cont < reinas:
        # Solicita al usuario la posición vertical y horizontal para una nueva reina
        posicionV = int(input("En qué posición vertical deseas colocar una reina? "))
        posicionH = int(input("En qué posición horizontal deseas colocar una reina? "))

        # Comprueba si la casilla está libre
        if matrix[posicionV][posicionH] not in ['R', 'x']:
            # Marca las casillas hacia adelante
            for fila in range(posicionV + 1, len(matrix)):
                nueva_fila = fila
                nueva_columna = posicionH
                matrix[nueva_fila][nueva_columna] = "x"

            # Marca las casillas hacia atrás
            for fila in range(posicionV - 1, -1, -1):
                nueva_fila = fila
                nueva_columna = posicionH
                matrix[nueva_fila][nueva_columna] = "x"

            # Marca las casillas hacia la derecha
            for columna in range(posicionH + 1, len(matrix[0])):
                nueva_fila = posicionV
                nueva_columna = columna
                matrix[nueva_fila][nueva_columna] = "x"

            # Marca las casillas hacia la izquierda
            for columna in range(posicionH - 1, -1, -1):
                nueva_fila = posicionV
                nueva_columna = columna
                matrix[nueva_fila][nueva_columna] = "x"

            # Diagonal izquierda-arriba a derecha-abajo
            for i in range(-min(posicionV, posicionH), min(len(matrix) - posicionV, len(matrix[0]) - posicionH)):
                nueva_fila = posicionV + i
                nueva_columna = posicionH + i
                matrix[nueva_fila][nueva_columna] = "x"

            # Diagonal derecha-arriba a izquierda-abajo
            for i in range(-min(posicionV, len(matrix[0]) - posicionH - 1), min(posicionV, posicionH + 1)):
                nueva_fila = posicionV + i
                nueva_columna = posicionH - i
                matrix[nueva_fila][nueva_columna] = "x"

            # Diagonal izquierda-abajo a derecha-arriba
            for i in range(-min(len(matrix) - posicionV - 1, posicionH), min(posicionV + 1, len(matrix[0]) - posicionH)):
                nueva_fila = posicionV - i
                nueva_columna = posicionH + i
                matrix[nueva_fila][nueva_columna] = "x"

            # Diagonal derecha-abajo a izquierda-arriba
            for i in range(-min(len(matrix) - posicionV - 1, len(matrix[0]) - posicionH - 1), min(posicionV + 1, posicionH + 1)):
                nueva_fila = posicionV - i
                nueva_columna = posicionH - i
                matrix[nueva_fila][nueva_columna] = "x"

            # Coloca la reina en la posición deseada
            matrix[posicionV][posicionH] = "R"

            # Imprime el tablero actualizado
            for fila in matrix:
                for casilla in fila:
                    print(casilla, end=' ')
                print()
            cont += 1
        else:
            print("Posición ya ocupada")

# Inicializa una matriz 8x8 para representar el tablero de ajedrez con todas las casillas vacías
matrix = []
for _ in range(8):
    fila = ['-'] * 8
    matrix.append(fila)

# Imprime el tablero vacío
for fila in matrix:
    for casilla in fila:
        print(casilla, end=' ')
    print()

# Solicita al usuario cuántas reinas desea colocar en el tablero y llama a la función "tablero" con ese número
reinas = int(input("¿Cuántas reinas deseas colocar? "))
tablero(reinas) # llama a la funcion tablero
