#Mediana de 3 números
import math
def medianaDeTresNumeros():
    n =0
    print('ingrese 3 numeros para calcular la mediana\n')
    lista = []
    while n<3:
        try:
            num = int(input('Ingrese un numero:\n'))
            #validamos si el dato ingresado es numero, por lo que devolvera TRUE si NO es numero al evaluar con math.isnan (not a number)
            if math.isnan(num) == False:
                lista.append(num)
                n = n + 1
            else:
                print('Ingrese un número valido\n')
        except:
            print('Error en el proceso\n\n')
    lista.sort()
    med = int(lista[1])
    print(f'La media de los numeros {lista} es : {med}\n')


def numeroPrimo():
    numero = int(input('Ingrese un número para determinar si es primo\n'))
    saberPrimo = numero
    if math.isnan(numero) == False:

        #proceso matematico para saber si es primo
        #Un número n es primo si y solo si (n-1)! + 1 es múltiplo de n

        saberPrimo= saberPrimo-1
        #determinamos factorial de numero-1
        fac = 1
        for x in range(1, saberPrimo+1):
            fac = fac * x
        multiplo=fac+1
        #comprobamos si es multiplo
        saberMultiplo = multiplo%numero
        if saberMultiplo == 0:
            print(f'El numero {numero} es Primo!\n')
        else:
            print(f'El número {numero} No es primo\n')
    else:
        print('error  al ingresar el valor\n')

def menu ():
    opcion =1
    while opcion == 1 or opcion == 2:
        opcion = int(input(
            '¿Que desea hacer?\n-Ingrese 1 para encontrar la media de 3 números\n-Ingrese 2 para saber si un número es primo\nCualquier otro número para salir\n'))

        if opcion == 1:
            medianaDeTresNumeros()
        elif opcion == 2:
            numeroPrimo()
        else:
            print('hasta pronto')

menu()