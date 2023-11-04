def multiplicacion_rusa(a, b): # declara la función con dos parametros
  # declaración de 3 arrays 
  array1 = [] # almacenara los valores de a dividido entre 2 
  array2 = [] # almacenara los valores de b multiplicados por 2
  array3 = [] # almacenará los numeros en la posición de los no pares

  array1.append(a) # agrega el valor de 'a' al array1 para comenzar a dividir
  while a > 0: # ciclo para divir mientras a sea mayor que 0
    a = a // 2 # a sera igual a la misma 'a' dividida entre dos
    array1.append(a) # agrega el nuevo valor de 'a' al array
    # variable que obtiene las veces que se dividio 'a' para multiplicar b la misma cantidad de veces
    cont = len(array1)

  array2.append(b) # agrega el valor de 'b' al array2 para comenzar a multiplicar
  while cont > 0: # mientras el contador sea mayor que 0, 'b' seguira multiplicandose
    b = b*2 # 'b' será igual a la misma 'b' multiplicada por 2
    array2.append(b) # agrega el nuevo valor de 'b' al array
    cont = cont - 1 # decrementa el contador para detener en algún punto las multiplicaciones
  for number in array1: # recorre todos los elementos del array1
    # modulo del elemento del array1 entre 2, buscando que sea diferente de 0, para obtener los no pares
    if number % 2 != 0:
      indice = array1.index(number) # obtiene el indice de un no par
    # agrega al array3 el numero del array2 que este en la posicion de un no par en array1
      array3.append(array2[indice])
  print(sum(array3)) # imprime la suma de todos los numeros en array3



a = int(input("Ingrese el primer número: ")) # pide la entrada de un numero entero
b = int(input("Ingrese el segundo número: ")) # pide la entrada de otro numero entero
multiplicacion_rusa(a, b) # llamada a la función con a y b como parametros
