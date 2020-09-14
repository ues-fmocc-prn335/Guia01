#INFORMACION
#ESTUDIANTE: CARLOS MANUEL MENDEZ MEDINA
#CARNET: MM18018

while True:
    print("--------------------MENU--------------------")
    try:
        opcion = int(input("Ingrese el numero del programa a ejecutar: \n1. Piramide \n2. Numero Primo \n3. Salir\nOpcion: "))
    except:
        print("Ingrese un numero valido.")
        if opcion < 1 or opcion > 3:
            print("Ingrese un numero entre 1 y 3")
        continue

    if opcion == 1:
        #CODIGO DE PIRAMIDE
        print("\n------------------CODIGO DE PIRAMIDE-------------------\n")
        #Manejo de excepciones
        while True:
            try:
                total_bloques = int(input("Ingrese el total de bloques: "))        
            except:
                print("Por favor, ingrese un numero valido")        
                continue
            if total_bloques <= 2:
                print("No es posible realizar una piramide con esta cantidad de bloques")
                total_bloques = 0
                continue
            break

        controlador = 1
        bloques = []
        acumulador = 1
        
        while controlador <= total_bloques:
            bloques.append("* "*acumulador)
            acumulador += 1
            controlador += acumulador
            
        bloques_usados = controlador - acumulador
        
        for fila in range(len(bloques)):
            espacios = len(bloques) - fila - 1
            print(" "*espacios + bloques[fila])
            
        print(f"{bloques_usados} bloques usados de {total_bloques}\n")
        #FIN CODIGO PIRAMIDE

    if opcion == 2:
        #CODIGO DE NUMERO PRIMO
        print("\n------------------CODIGO DE NUMERO PRIMO-------------------\n")
        #Manejo de errores
        while True:
            try:
                numero = int(input("Ingrese un numero entero: "))
            except:
                print("Ingrese un numero valido")
                continue
            break
        
        acumulador = 0
        for contador in range(1, numero+1):
            if numero % contador == 0:
                acumulador += 1
        
        if acumulador == 2:
            print(f"{numero} es primo \n")
        else:
            print(f"{numero} no es primo \n")
        #FIN CODIGO NUMERO PRIMO
    
    if opcion == 3:
        break

    