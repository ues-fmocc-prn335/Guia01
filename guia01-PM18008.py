# metodo para formar piramide con n bloques
def piramide():
    num = input('Ingrese el numero de bloques: ')

    try:
        n = int(num)
    except:
        print('valor no valido')
        quit()

    ite = 0
    while n > ite:
        ite = ite + 1
        n = n - ite

    nivel = 1
    while nivel <= ite:
        print(' ' * (ite - nivel + 1), '* ' * nivel, sep='')
        nivel = nivel + 1
    print('* ' * n, sep='')
    print('Se forma la piramide completa hasta el nivel:', ite)

# Numero entero primo
def num_primo():
    num = input('Ingrese el numero: ')

    try:
        n = int(num)
    except:
        print('El valor:', num, 'no es un entero')
        quit()

    for i in range(2, n):
        if n % i == 0:
            print('El numero', n, 'no es primo')
            quit()

    print('El numero', n, 'es primo')

op = input('Ingrese su opcion\n1. piramide\n2. num primo\nOtro. salir\n')

if op=='1':
    piramide()
elif op=='2':
    num_primo()
else:
    print('Terminado')
