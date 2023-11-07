def hanoi(n, destino, auxiliar):
    len_n = len(n)
    if len_n == 0:
        print("No hay discos en la torre de origen")
    elif len_n == 1:
        nodo = n[0]
        destino.append(nodo)
        n.pop(0)
        return "la torre destino final es: ", destino
    else:
        nodo = n[0]
        destino.append(nodo)
        n.pop(0)
        return hanoi(n, destino, auxiliar)


n = [1,2,3,4,5]
destino = []
auxiliar = []
print(hanoi(n,destino, auxiliar))
