
# Cardona Valle, Henry Rolando CV19014

import os

def Ejercicios():
    os.system('cls')
    print("Selecciona una opción \n")
    print("1- Crear una piramide con bloques.\n")
    print("2- Calcular la mediana de tres números.\n")
    print("3- Salir.\n")

def Salir():
    print("Desea salir o continuar: \n")
    print("1- Continuar.\n")
    print("2- Salir.\n")

while True:
    Ejercicios()
    Opcion = input("Inserte la opción que escogio: ")

    #Ejercicio 1
    if Opcion == "1":
        Bloques = 1
        Dato = int(input("\n Ingrese el número de bloques: "))
        while Dato >= Bloques:
            Dato_Mostrar = " *" * Bloques
            print(Dato_Mostrar.center(100))
            Dato = Dato - Bloques
            Bloques = Bloques + 1
        if Dato > 0:
            print("\n  Esta es la cantidad de bloques sobrantes " + repr(Dato))
        else:
            print("\n No te sobraron bloques")

    #Ejercicio 2
    if Opcion == "2":
        Numero1 = int(input("\n Ingrese el primer número: "))
        Numero2 = int(input("\n Ingrese el segundo número: "))
        Numero3 = int(input("\n Ingrese el tercer número: "))
        Suma = Numero1 + Numero2 + Numero3
        print("La media es: " + str(Suma / 3))

    Salir()
    Opcion = input("\n Inserte la opción que escogio: ")

    if Opcion == "2":
        break


