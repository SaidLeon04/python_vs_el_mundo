def hanoi(n, origen, auxiliar, destino): # función principal
    if n == 1: # si el número de discos es 1
        print(f"Mover disco 1 desde {origen} hacia {destino}") # muestra el movimiento
        mover_disco(origen, destino) # llama a la función mover_disco
        return # retorna
    hanoi(n-1, origen, destino, auxiliar) # llama a la función hanoi disminuyendo el número de discos
    print(f"Mover disco {n} desde {origen} hacia {destino}") # muestra el movimiento
    mover_disco(origen, destino) # llama a la función mover_disco 
    hanoi(n-1, auxiliar, origen, destino) # llama a la función hanoi disminuyendo el número de discos

def mover_disco(origen, destino): # función para mover el disco
    disco = pilas[origen].pop() # quita el disco de la pila de origen
    pilas[destino].append(disco) #  agrega el disco a la pila de destino
    actual() # llama a la función actual

def actual(): # función para mostrar el estado actual
    print("Torre 1: ", pilas['A']) # muestra la pila A
    print("Torre 2: ", pilas['B']) # muestra la pila B
    print("Torre 3: ", pilas['C']) # muestra la pila C
    print() # imprime un salto de línea


pilas = {'A': [5, 4, 3, 2, 1], 'B': [], 'C': []} # declaracion de las 3 pilas o torres

# Imprimir estado inicial
print("Estado inicial:") # muestra el estado inicial
actual() # llama a la función para mostrar el estado en cada movimiento

# Llamar a la función principal para resolver las Torres de Hanoi
hanoi(5, 'A', 'B', 'C')
