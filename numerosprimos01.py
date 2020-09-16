import math


def es_primo(numero):

    if (numero <= 1):
        return False

    for i in range(2, math.ceil(math.sqrt(numero)) + 1):
        if (numero % i == 0 and i != numero):
            return False
    return True


while True:
    try:
        numero = int(input("inserta un numero (0) salir >> "))
        if numero == 0:
            break
        if es_primo(numero):
            print("\nEl numero %s es primo" % numero)
        else:
            print("\nEl numero %s NO es primo" % numero)
    except:
        print("\nEl numero tiene que ser entero")
