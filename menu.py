# importo las funciones
import conversion as conv
import primo as pr


def menu():
    while True:

# Muestro las opciones del menu
        opcion = int(input("\nBIENVENIDO\n¿Que desea realizar?\n"
                           "1.Convertir de Decimal a Binario\n"
                           "2.Verificar si un numero es Primo\n"
                           "3.Salir\n"))

# Si la opcion fue 1
        if (opcion == 1):
            print(conv.Convertir(int(input("Introduce el número a convertir a binario: "))))

# Si la opcion fue 2
        if (opcion == 2):
            numero = int(input("Ingrese un numero "))

# valido que sea primo o no
            if pr.Primo(numero):
                print("El numero %s es primo" % numero)
                break
            else:
                print("El numero %s NO es primo" % numero)

# si la opcion es la 3
        if (opcion == 3):
            print("Adios ... .. .")
            break
menu()
