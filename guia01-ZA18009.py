#Nombre: Zarco Alvarenga, Harold Jose
#Carnet: ZA18009

print("Bienvenido\n")
opcion = int(input("Ingrese el programa a ejecutar: \n1. Evaluar numero primo \n2. Centrar mensajes \n3. Salir\nOpcion: "))

#Codigo Numero Primo
if opcion == 1:
    #valor entero que se evaluara
    numero = int(input("Ingrese numero a evaluar: "))
    #aumentando en 1 el valor de numero para recorrer el ciclo for
    max=numero+1

    contador = 0

    for i in range(1,max):
        #Si el residuo es = 0 el contador aumentara en +1
        if numero%i == 0:
            contador += 1

    #Si el contador aumenta mas de 2 veces no sera primo
    if contador==2:
        print("El numero " + str(numero) + " es primo")
    else:
        print("El numero " + str(numero) + " no es primo")

#Codigo Centrar Mensaje
if opcion == 2:
    #Se solicita al usuario el tamaño que tendra la "pagina".
    tamanio=int(input("Ingrese el tamaño de la pagina: "))

    palabra=input("Ingrese la palabra: ")

    print("Tamaño de la palabra: " + str(len(palabra)))
    lados=tamanio-len(palabra)
    print("Espacios restantes: " + str(lados))

    div=lados/2

    if lados%2==0:
        print("Espacios a derecha: " + str(div) + "\nEspacios a izquierda: " + str(div))
    else:
        print("Espacios a derecha: " + str(div-0.5) + "\nEspacios a izquierda: " + str(div+0.5))

    print("Palabra centrada: \n")

    print(palabra.center(tamanio))

if opcion==3:
    print("Salio del programa")
