

class nodoArbol(object):
    def __init__(self, info):
        self.izq = None
        self.der = None
        self.info = info
    
def eliminar_nodo(raiz, clave):
    x = None
    if raiz is not None:
        if(clave < raiz.info):
            raiz.izq, x = eliminar_nodo(raiz.izq, clave)
        elif (clave > raiz.info):
            raiz.der, x = eliminar_nodo(raiz.der, clave)
        else:
            x = raiz.info
            if raiz.izq is None:
                raiz = raiz.der
            elif raiz.der is None:
                raiz = raiz.izq
            else:
                raiz.izq, aux = reemplazar(raiz.izq)
                raiz.info = aux.info
    return raiz, x

def insertar_nodo(raiz, dato):
    if raiz is None:
        raiz = nodoArbol(dato)
    elif dato < raiz.info:
        raiz.izq = insertar_nodo(raiz.izq, dato)
    else:
        raiz.der = insertar_nodo(raiz.der, dato)
    return raiz

def arbolvacio(raiz):
    return raiz is None

def reemplazar(raiz):
    aux = None
    if raiz.der is None:
        aux = raiz
        raiz = raiz.izq
    else:
        raiz.der, aux = reemplazar(raiz.der)
    return raiz, aux

def por_nivel(raiz):
    pendientes = Cola()
    arribo(pendientes, raiz)
    while not cola_vacia(pendientes):
        nodo = atencion(pendientes)
        print(nodo.info)
        if nodo.izq is not None:
            arribo(pendientes, nodo.izq)
        if nodo.der is not None:
            arribo(pendientes, nodo.der)

def buscar(raiz,clave):
    pos = None
    if raiz is not None:
        if raiz.info == clave:
            pos = raiz
        elif clave < raiz.info:
            pos = buscar(raiz.izq,clave)
        else:
            pos = buscar(raiz.der,clave)
    return pos

def inorden(raiz):
    if raiz is not None:
        inorden(raiz.izq)
        print(raiz.info)
        inorden(raiz.der)
def preorden(raiz):
    if raiz is not None:
        print(raiz.info)
        preorden(raiz.izq)
        preorden(raiz.der)

def postorden(raiz):
    if raiz is not None:
        postorden(raiz.der)
        print(raiz.info)
        postorden(raiz.izq)

def arbol_actual(raiz):
    print("Arbol actual:")
    if raiz is not None:
        print("Raiz:", raiz.info)
        print("Subarbol izquierdo:", raiz.izq.info)
        print("Subarbol derecho:", raiz.der.info)
    else:
        print("Arbol vacio")
  

NodoArbol = nodoArbol(10)
while True:
    print("Opciones")
    print("1. Eliminar nodo")
    print("2. Insertar nodo")
    print("3. Arbol vacio")
    print("4. Reemplazar")
    print("5. Por nivel")
    print("6. Buscar nodo")
    print("7. Recorridos")
    print("8. Salir")
    opcion = input("Ingrese una opcion: ")

    if opcion == "1":
        dato = int(input("Ingrese el numero a eliminar: "))
        eliminar_nodo(NodoArbol, dato)
    elif opcion == "2":
        dato = int(input("Ingrese un numero: "))
        insertar_nodo(NodoArbol, dato)
    elif opcion == "3":
        if arbolvacio(NodoArbol):
            print("El arbol esta vacio")
        else:
            print("El arbol no esta vacio")
    elif opcion == "4":
        dato = int(input("Ingrese el numero a reemplazar: "))
        reemplazar(NodoArbol, dato)
    elif opcion == "5":
        # por_nivel(NodoArbol)
        print("Por nivel")
    elif opcion == "6":
        dato = int(input("Ingrese el numero a buscar: "))
        buscar(NodoArbol, dato)
    elif opcion == "7":
        print("Recorridos")
        print("1. Inorden")
        print("2. Preorden")
        print("3. Postorden")
        opcion = input("Ingrese una opcion: ")
        if opcion == "1":
            inorden(NodoArbol)
        elif opcion == "2":
            preorden(NodoArbol)
        elif opcion == "3":
            postorden(NodoArbol)
    elif opcion == "8":
        break