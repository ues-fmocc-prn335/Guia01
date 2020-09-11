import os
opcion = 0
while opcion == 0 :
    os.system ("cls") #Borrando pantalla
    try:
        opcion = int(input("¿Qué desea ver?\n1. Resolución de la piramide\n2. Resolución de la mediana de 3 números\n3. Salir\n"))

        if opcion < 1 or opcion > 3:
            opcion=0
            print("Ingrese una opción válida")
            
            os.system ("cls") #Borrando pantalla 
    except:
        opcion = 0
        print("Ingrese una opción válida")
        
        os.system ("cls") #Borrando pantalla
    if opcion == 3:
        print("ADIOS!!!")
        quit() #Saliendo del programa por petición del usuario
    # NIVELES DE UNA PIRAMIDE , DETERMINADA POR EL NÚMERO DE BLOQUES:

    while opcion == 1:
        os.system ("cls") #Borrando pantalla
        try:
            blocks = int(input("ingrese la cantidaad de bloques"))
        except:
            blocks = -1
        if blocks <= 0:
            if blocks == -1:
                print(f"Ingrese números !!")
            else:
                print(f"No se puede construir la piramide con {blocks} bloques")
        else:
            opcion=0 #asegurando la repetición del primer WHILE
            for i in range(blocks):
                print(" " * (60 - (3 * (i + 1))), " ████ "*(i+1))
                blocks -= (i+1)
                if blocks < (i+2):
                    print(f"Sobran {blocks} bloques, la piramide formada tien {i+1} niveles")
                    break
    # MEDIANA DE 3 NÚMEROS:

    while opcion == 2:
        os.system ("cls") #Borrando pantalla
        lst = list()
        for i in range(3):
            try:
                numero = input(f"{i+1}.Digite un numero ")
                lst.append(int(numero))
            except:
                lst = list()
        if len(lst) < 3:
            print("Error, no se admiten letras ....Digite números!! ")
        else:
            opcion=0
            lst.sort()
            bolean = True
            print(f"La mediana de {lst} es {lst[1]}")
