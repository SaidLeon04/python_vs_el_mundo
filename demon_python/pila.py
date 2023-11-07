class NodoPila:
    def __init__(self, info):
        self.info = info
        self.sig = None

class Pila:
    def __init__(self):
        self.cima = None
        self.tamanio = 0

    def apilar(pila, dato):
        nodo = NodoPila(dato)
        nodo.info = dato
        nodo.sig = pila.cima
        pila.cima = nodo
        pila.tamanio += 1

    def desapilar(pila):
        x = pila.cima.info
        pila.cima = pila.cima.sig
        pila.tamanio -= 1
        return x

    def pila_vacia(pila):
        return pila.cima is None

    def en_cima(pila):
        if pila.cima is not None:
            return pila.cima.info
        else:
            return None

    def obtener_tamanio(pila):
        return pila.tamanio

# Interacción con el usuario
pila = Pila()
while True:
    print("Opciones:")
    print("1. Apilar")
    print("2. Desapilar")
    print("3. Mostrar la cima")
    print("4. Mostrar el tamaño")
    print("5. Ver pila")
    print("6. Salir")
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        dato = input("Ingrese el valor a apilar: ")
        pila.apilar(dato)
    elif opcion == "2":
        elemento = pila.desapilar()
        if elemento is not None:
            print("Elemento desapilado:", elemento)
        else:
            print("La pila está vacía.")
    elif opcion == "3":
        cima = pila.en_cima()
        if cima is not None:
            print("Cima de la pila:", cima)
        else:
            print("La pila está vacía.")
    elif opcion == "4":
        tamaño = pila.obtener_tamanio()
        print("Tamaño de la pila:", tamaño)
    elif opcion == "5":
        print("pila actual: ", pila)
    elif opcion == "6":
        break
    else:
        print("Opción no válida. Por favor, elija una opción válida.")
