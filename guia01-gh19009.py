#funcion para piramide
def piramide (bloque):
    bloques = 1; i = 1
    espacio = bloque
    #la variable i llevara la cuenta de cuantos bloques se estan imprimiendo
    #la variable espacio dará el centrado a la piramide y la variable bloques es un contador

    while (i <= bloque):
        print (" "*espacio, "* "*bloques, " "*espacio, "\n")
        espacio -= 1
        bloques += 1
        i +=bloques
   
    print (f"Sobraron {(bloques+bloque)-i} bloques") 

#funcion para determinar número primo
def primo(priMo):
    divisores = 1
    #la variables divisores llevara la cuenta de cuantos divisores posee el numero a evaluar

    for i in range (1,priMo):
        #si el mod es igual a 0 es porque encontro un divisor
        if((priMo%i) == 0):
            divisores += 1

    if (divisores == 2):
        print(f"El numero {priMo} es primo")  
    else:
        print(f"El numero {priMo} no es primo")

#funcion para validar opcion ingresada por el usuario
def validarOpcion (valor):
    valor = input("Ingrese numero de opcion:\n1.Hacer una piramide\n2.Determinar un numero primo\nCualquier numero para salir\n")
    while True:
        if(valor.isdigit()):
            valor = int(valor)
            return valor
            break
        else:
            print("Debe ingresar un entero")

#valida el inicio del menu
while True:
    opcion = input("Ingrese numero de opcion:\n1.Hacer una piramide\n2.Determinar un numero primo\n")
    try:
        opcion = int(opcion)
    except ValueError:
        print("Debe ingresar un entero")

    if(opcion == 1 or opcion == 2):
        break
    else:
        print("Tiene que ingresar 1 o 2")

#menu
while (opcion == 1 or opcion ==2):
    if(opcion == 1):
        #llamado a la funcion piramide
        numBloques = input("Ingrese numero de bloques: ")

        if(numBloques.isdigit()):
            piramide(int(numBloques))
            opcion = validarOpcion(opcion)
        else:
            print("Tiene que ingresar un entero")

    elif (opcion == 2):
        #llamando a la funcion primo
        numPrimo = input("Ingrese un numero: ")

        if(numPrimo.isdigit()):
            primo(int(numPrimo))
            opcion = validarOpcion(opcion)
        else:
            print("Tiene que ingresar un entero")

print("Adiós!")




