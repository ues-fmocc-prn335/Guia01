#Carnet:CF18020 Nombre:Castro Flores Mauricio Enrique
menu=int(input("Escriba el ListaNumero de ejercicio a usar\n1.Piramide\n2.Mediana\n3.No hacer nada\n"))
if menu == 1:
    # Piramide
    try:
        blockes = int(input("Cuantos blockes quiere para su piramide\n"))
        sobra = True
        if blockes > 2:
            for b in range(blockes):
                if (b * (b + 1) / 2) == blockes:
                    for i in range(1, b + 1):
                        print(" " * (b - i), end="")
                        print("▬" * i)
                    sobra = False
                elif (b * (b + 1) / 2) > blockes and sobra == True:
                    contador = 0
                    for i in range(1, b):
                        print(" " * (b - i), end="")
                        print("▬" * i)
                        contador = contador + i
                    print("Sobran:", blockes - contador, " blockes")
                    break
        else:
            print("Por favor ingrese un ListaNumero mayor a 2")
    except ValueError as e:
        print("ERROR: ", e)
    menu = int(input("\nEscriba el ListaNumero de ejercicio a usar\n1.Piramide\n2.Mediana\n3.No hacer nada\n"))
elif menu == 2:
    #Mediana de 3 numeros
    ListaNumeros = []
    for i in range(3):
        ListaNumeros.append(input("Ingrese numero\n"))
    print("\nIngresaste ", ListaNumeros[0], ListaNumeros[1], ListaNumeros[2])
    print("\nLa mediana es ", int(ListaNumeros[1]))
    menu = int(input("\nEscriba el ListaNumero de ejercicio a usar\n1.Piramide\n2.Mediana\n3.No hacer nada\n"))

while menu <3 and menu>0:
    if menu == 1:
        try:
            blockes = int(input("\nCuantos blockes quiere para su piramide\n"))
            sobra = True
            if blockes > 2:
                for b in range(blockes):
                    if (b * (b + 1) / 2) == blockes:
                        for i in range(1, b + 1):
                            print(" " * (b - i), end="")
                            print("▬" * i)
                        sobra = False
                    elif (b * (b + 1) / 2) > blockes and sobra == True:
                        contador = 0
                        for i in range(1, b):
                            print(" " * (b - i), end="")
                            print("▬" * i)
                            contador = contador + i
                        print("Sobran:", blockes - contador, " blockes")
                        break
            else:
                print("Por favor ingrese un ListaNumero mayor a 2")
        except ValueError as e:
            print("ERROR: ", e)
    elif menu == 2:
        ListaNumeros = []
        for i in range(3):
            ListaNumeros.append(input("\nIngrese numero\n"))
        print("\nIngresaste ", ListaNumeros[0], ListaNumeros[1], ListaNumeros[2])
        print("\nLa mediana es ", int(ListaNumeros[1]))
    menu = int(input("\nEscriba el ListaNumero de ejercicio a usar\n1.Piramide\n2.Suma\n"))