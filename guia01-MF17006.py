def numPrimo():
    num = input("Ingrese un numero: ")
    contador = 0
    for i in range (2, (int(num) + 1)):
        if int(num) % int(i) == 0:
            contador = contador + 1

    if contador == 2:
        return print("Es primo")
    else:
        return print("No es primo")

def mcd(a, b):
    if b == 0:
        return a
    else:
        if mcd(b, a%b) == None:
            print("")
        else:
            return print(mcd(b, a % b))


menu = int(input("Seleccione una opcion:\n1. Numero Primo\n2. MCD\nOtro numero para salir\n"))
while menu >= 1 and menu <= 2:
    if menu == 1:
        numPrimo()
        menu = int(input("Seleccione una opcion:\n1. Numero Primo\n2. MCD\nOtro numero para salir\n"))
    elif menu == 2:
        a = int(input("Ingrese el numero a:\n"))
        b = int(input("Ingrese el numero b:\n"))
        print("MCD es: \n")
        mcd(a, b)
        menu = int(input("Seleccione una opcion:\n1. Numero Primo\n2. MCD\nOtro numero para salir\n"))
    else:
        break

