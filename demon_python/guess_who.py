
array_guisantes = ["repetidora", "lanzaguisantes", "hielaguisantes", 
                       "lanzaguisantes de fuego", "tripitidora", 
                       "lanzaguisantes primitivo"]
    
array_instantaneas = ["petaseta", "patatapum", "patatapum primitiva", 
                          "petacereza", "jalapeño", "pepino tactico"]
    
array_solar = ["girasol", "birasol","seta solar", 
                   "tomate solar", "hongo solar","girasol primitivo"]
    
array_dino = ["platanosaurio", "aloesaurio", "zanahoriatops",
                  "velocirabano","ave del paraiso", "apapasaurio"]

# instrucciones
print(" -Adivina quien pero son Plantas de pvz- \n\n")
print("Elige una planta de las siguientes: \n")
for elemento in [array_solar, array_dino, array_guisantes, array_instantaneas]:
    print(elemento)
    print() 

print("Como avanzar? \n1 = SI o 2 = NO \n \n")


op = int(input("La planta que has elegido es de tipo guisante? "))
if op == 1:
    op = int(input("La planta que has elegido tiene 3 cabezas? "))
    if op == 1:
        print("Tripitidora")
    else:
        op = int(input("la planta que has elegido dispara dos guisantes? "))
        if op == 2:
            op = int(input("La planta que has elegido es de tipo hielo? "))
            if op == 1:
                print("hielaguisantes")
            else:
                op = int(input("La planta que has elegido es de tipo fuego? "))
                if op == 1:
                    print("lanzaguisantes de fuego")
                else:
                    op = int(input("La planta que has elegido es de tipo primitivo? "))
                    if op == 1:
                        print("lanzaguisantes primitivo")
                    else:
                        print("lanzaguisantes")
        else:
            print("repetidora")
    

elif op == 2:
    op = int(input("La planta que has elegido es de tipo instantanea? "))
    if op == 1:
        op = int(input("La planta que has elegido es de pvz heroes o pvz chino? "))
        if op == 1:
            print("pepino tactico")
        else:
            op = int(input("La planta que has elegido es una verdura? "))
            if op == 1:
                print("jalapeño")
            else:
                op = int(input("La planta que has elegido crea una masacre? "))
                if op == 1:
                    print("petaseta")
                else:
                    op = int(input("La planta que has elegido es primitiva? "))
                    if op == 1:
                        print("patatapum primitiva")
                    else:
                        op = int(input("La planta que has elegido tiene dos cabezas? "))
                        if op == 1:
                            print("petacereza")
                        else:
                            print("patatapum")
    elif op == 2:        
        op = int(input("La planta que has elegido es de tipo solar? "))
        if op == 1:
            op = int(input("La planta que has elegido es lleva solar en su nombre? "))
            if op == 1:
                op = int(input("La planta que has elegido es una verdura? "))
                if op == 1:
                    print("tomate solar")
                else:
                    op = int(input("La planta que has elegido es una seta? "))
                    if op == 1:
                        print("seta solar")
                    else:
                        print("hongo solar")
            else:
                op = int(input("La planta que has elegido es primitiva? "))
                if op == 1:
                    print("girasol primitivo")
                else:
                    op = int(input("La planta que has elegido tiene dos cabezas? "))
                    if op == 1:
                        print("birasol")
                    else:
                        print("girasol")

        elif op == 2:
            op = int(input("La planta que has elegido es un ave? "))
            if op == 1:
                print("ave del paraiso")
            else:
                op = int(input("La planta que has elegido es una fruta? "))
                if op == 1:
                    print("platanosaurio")
                else:
                    op = int(input("La planta que has elegido genera dos plantas de si mismo? "))
                    if op == 1:
                        print("velocirrabano")
                    else:
                        op = int(input("La planta que has elegido es un tuberculo? "))
                        if op == 1:
                            print("apapasaurio")
                        else: 
                            op = int(input("La planta que has elegido es curativa? "))
                            if op == 1:
                                print("aloesaurio")
                            else:
                                print("zanahoriatops")
            
        
