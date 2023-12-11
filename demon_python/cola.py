class nodoCola(object):
    info, sig = None, None

class Cola(object):

    def __init__(self):
        self.frente = None
        self.final = None
        self.tamanio = 0

    def arribo(cola, dato):
        nodo = nodoCola()
        nodo.info = dato
        if cola.frente == None:
            cola.frente = nodo
        else:
            cola.final.sig = nodo
        cola.final = nodo
        cola.tamanio += 1

    def atencion(cola):
        dato = cola.frente.info
        cola.frente = cola.frente.sig
        if cola.frente == None:
            cola.final = None
        cola.tamanio -= 1
        return dato

    def cola_vacia(cola):
        return cola.frente == None
    
    def en_frente(cola):
        return cola.frente.info
    
    def tamanio(cola):
        return cola.tamanio
    """
    def mover_al_final(cola):
        dato = atencion(cola)
        arribo(cola, dato)
        return dato
    """