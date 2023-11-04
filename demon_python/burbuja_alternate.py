lista = [12,2,33,55,8,98,4,32,32,12,89,0]
n = len(lista)
for i in range(n - 1):
    for j in range(0, n - i - 1):

        if lista[j] < lista[j + 1]:
            lista[j + 1], lista[j] =  lista[j],lista[j + 1]

print(lista)
