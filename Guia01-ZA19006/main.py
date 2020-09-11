"""Guía 01 PRN335
Alumna: Zepeda Arriola, María de los Ángeles ZA19006
Primer código: Pirámide a  partir del número de bloques que el usuario ingresa, tomando en cuenta
que si los bloques no son exactos para formar un nivel se realiza con la mínima cantidad requerida
Segundo código: Encontrar el MCD de tres números ingresados por el usuario"""

import math


def pyramid(numbloq):
    # El número de bloques se rige por suma de Gauss
    # suma=(0.5)(n)(n+1) siendo la suma la cantidad total de bloques y n el número de bloques del nivel inferior
    # Se puede resolver entonces la ecuación cuadrática resultante de la expresión anterior
    # ->2suma= n*n+n --> n*n+n-2*suma=0
    # Sea d es el discriminante, y los valores de n será una de las dos posibles raíces de la ecuación anterior
    # Se tomará el valor positivo, dado que estamos hablando de un número de bloques
    d = int(1 + 8 * numbloq)
    nivel = int((-1 + math.sqrt(d)) / 2)
    sobrante = int(numbloq - 0.5 * nivel * (nivel + 1))
    for x in range(nivel):
        print("  " * (nivel - x), end="")
        print(" *  " * (x + 1))
    print(f"Sobraron {sobrante} que no se incluyeron en la pirámide")


def mcd(num1, num2, num3):
    maxcd = 1
    # Se calculará el menor de los tres números, para conocer el límite hasta el cual se va a comparar
    if num1 < num2:
        if num1 < num3:
            menor = num1
        else:
            menor = num3
    elif num2 < num1:
        if num2 < num3:
            menor = num2
        else:
            menor = num3
    else:
        if num1 < num3:
            menor = num1
        else:
            menor = num3

    for x in range(int(menor + 1)):
        if (num1 % (x + 1) == 0) and (num2 % (x + 1) == 0) and (num3 % (x + 1) == 0):
            # Según la definición, el MCD es el mayor de los divisores, es por ello que cada vez que entre a esta
            # condición (entrará si (x+1) es divisor de los tres números) se va a igualar al valor del último divisor
            maxcd = (x + 1)
    return maxcd


if __name__ == '__main__':
    print("Escoja un número en el menú")
    try:
        num = int(input("Menú: 1. Pirámide 2.MCD de tres números\n"))
        if num == 1:
            correcto = True
            try:
                # Si ingresa decimal, solo se toma la parte entera
                blocks = int(input("Ingrese el número de bloques para construir la pirámide\n"))
            except ValueError:
                correcto = False
            if correcto:
                if blocks > 0:
                    pyramid(blocks)
                else:
                    print("Error en el número de bloques")
            else:
                print("Recuerde que solo puede ingresar variables de tipo int")
        elif num == 2:
            print("Ingrese 3 números enteros")
            correcto = True
            try:
                # Si ingresa decimal solo toma la parte entera
                numero1 = int(input("Primer número\n"))
                numero2 = int(input("Segundo número\n"))
                numero3 = int(input("Tercer número\n"))
            except ValueError:
                correcto = False

            if correcto:
                if (numero1 > 0) and (numero2 > 0) and (numero3 > 0):
                    print("El MCD de los números ingresados es:", mcd(numero1, numero2, numero3))
                else:
                    print("Recuerde que solamente puede ingresar enteros positivos")
            else:
                print("Solamente puede ingresar enteros : variables tipo int")
        else:
            print("Error. Debe ingresar 1 o 2 para poder acceder a una de las funciones del programa")
    except ValueError:
        print("Error en la opción escogida en el menú, solamente puede ingresar 1 o 2")