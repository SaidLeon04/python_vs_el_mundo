class NodoPila: # clase para cada nodo de la pila
    def __init__(self, info): # constructor de la clase
        self.info = info # almacena el elemento
        self.sig = None # almacena el siguiente nodo como NONE

class Pila: # clase para la pila
    def __init__(self): # constructor de la clase
        self.cima = None # asigna el valor a la cima
        self.tamanio = 0 # inicializa el tamaño de la pila

    def apilar(pila, dato): # método para apilar
        nodo = NodoPila(dato) # crea un nodo con el dato
        nodo.info = dato # asigna el dato al nodo
        nodo.sig = pila.cima # asigna la cima a la siguiente posición
        pila.cima = nodo # asigna el nodo a la cima
        pila.tamanio += 1   # incrementa el tamaño de la pila

    def desapilar(pila): # método para desapilar
        x = pila.cima.info # almacena el dato de la cima
        pila.cima = pila.cima.sig # asigna el siguiente nodo a la cima
        pila.tamanio -= 1 # decrementa el tamaño de la pila
        return x   # retorna el dato de la cima

    def pila_vacia(pila): # método para verificar si la pila está vacía
        return pila.cima is None # retorna True si la cima es NONE

    def en_cima(pila): # método para obtener el dato de la cima
        if pila.cima is not None:   # si la cima no es NONE
            return pila.cima.info  # retorna el dato de la cima
        else: # caso contrario
            return None # retorna NONE

    def obtener_tamanio(pila): # método para obtener el tamaño de la pila
        return pila.tamanio #retorna el tamaño de la pila
    
    def imprimir_pila(pila):
        print("Pila actual:")
        nodo_actual = pila.cima
        while nodo_actual is not None:
            print(nodo_actual.info)
            nodo_actual = nodo_actual.sig
        print("----")

# Menu
pila = Pila() # crea un objeto de la clase Pila
while True: # ciclo para el menú
    print("Opciones:") # muestra las opciones
    print("1. Apilar")
    print("2. Desapilar")
    print("3. Mostrar la cima")
    print("4. Mostrar el tamaño")
    print("5. Mostrar la pila")
    print("6. Salir")
    opcion = input("Seleccione una opción: ") # pide la entrada del usuario

    if opcion == "1": # si la opción es 1
        dato = input("Ingrese el valor a apilar: ") # pide el dato a apilar
        pila.apilar(dato) # llama al método apilar
        pila.imprimir_pila()
    elif opcion == "2": # si la opción es 2
        elemento = pila.desapilar() # llama al método desapilar
        if elemento is not None: # si el elemento no es NONE
            print("Elemento desapilado:", elemento) # muestra el elemento
            pila.imprimir_pila()
        else: # caso contrario
            print("La pila está vacía.")
            pila.imprimir_pila()
    elif opcion == "3":  # si la opción es 3
        cima = pila.en_cima() # llama al método en_cima
        if cima is not None: # si la cima no es NONE
            print("Cima de la pila:", cima) # muestra la cima
            pila.imprimir_pila()
        else: # caso contrario
            print("La pila está vacía.")
            pila.imprimir_pila()
    elif opcion == "4": # si la opción es 4
        tamaño = pila.obtener_tamanio() # llama al método obtener_tamanio
        print("Tamaño de la pila:", tamaño) # muestra el tamaño
        pila.imprimir_pila()
    elif opcion == "5":
        print("Pila actual: ")
        pila.imprimir_pila()
    elif opcion == "6": # si la opción es 5
        break # rompe el ciclo
    else: # caso contrario
        print("Opción no válida")
