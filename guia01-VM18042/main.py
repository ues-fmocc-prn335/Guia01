#Vargas Moran, Mauricio Enrique
#VM18042

def mediana():

    # declarando la lista
    numeros = []

    # creando el for para ingresar los numeros en la lista
    for i in range(3):
        numeros.append(int(input("Ingresa los numeros\n")))

    # imprimiendo la lista en el orden que dio el usuario
    print("Tus numero son: ", numeros[0], numeros[1], numeros[2])

    # funcion que ordena los numeros de menor a mayor(cortesia de ale y armando)
    numeros.sort()

    # imprimiendo la lista ya ordenanda
    print(numeros)

    print("La mediana es ", int(numeros[1]))



def binarios():
    # ingresando el numero para convertirlo a binario
    numerodecimal = int(input("Inserte un numero para convetirlo:"))

    # usando la funcion format para convertir a vinario e imprimirlo
    print(format(numerodecimal, "0b"))




i=int(input("Seleccione una opcion\n1.La mediana\n2.Binario\n3.Salir"))
while(i==1 or i==2):
    if(i==1):
        mediana()
    elif(i==2):
       binarios()
    else:
        print("Hasta luego")
        break
    i = int(input("Seleccione una opcion\n1.La mediana\n2.Binario\n3.Salir"))
