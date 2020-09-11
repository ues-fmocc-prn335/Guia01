def primo():
    numero = int(input("ingrese el numero que desea saber si es primo\n"))
    acum = 0
    for cont in range(1, numero + 1):
        if numero % cont == 0:
            acum = acum + 1
    if acum == 2:
        print("el numero:", numero, "es primo")
    else:
        print("el numero:", numero, "no es primo")

def centrado():
    espacios = int(input("ingrese el numero de tamaño de la pagina\n"))
    palabra = input("ingrese lo que desea escribir en ella\n")
    inicio = (espacios / 2) - ((len(palabra)) / 2)
    print(" " * (int(inicio)), palabra)

opcion=int(input("elija la opcion que desea\n1-Primo\n2-Centrar\n"))
while(opcion==1 or opcion==2):
    if(opcion==1):
        primo()
    elif(opcion==2):
        centrado()
    else:
        print("Adios que tenga un buen dia :)")
    opcion = int(input("elija la opcion que desea\n1-Primo\n2-Centrar"))