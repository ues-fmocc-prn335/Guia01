# William Giovanni Cheverría Pacheco
# CP11023

# 1-Verfica si es primo
def primo(num):
    count = 0
    if num > 1:
        for i in range(num):
            if num % (i + 1) == 0:
                count = count + 1

        # Si es divisible por el mismo y uno entonces nos da dos
        if count == 2:
            print('\n<<RESULTADO>>\nSi es primo.')
        else:
            print('\n<<RESULTADO>>\nNo es primo.')

    else:
        print('\nLos numeros negativos no son primos por definicion,ni tampoco cero y ni uno.')


# 2-piramide de niveles por bloques
def piramide(bloques):
    niveles = 0
    bloques_por_nivel = 0
    bloques_sobrantes = 0
    contador = 0

    # calculando niveles a traves de los bloques ingresados por el usuario
    while bloques > bloques_por_nivel:
        contador = contador + 1
        bloques_por_nivel = bloques_por_nivel + contador

        if bloques_por_nivel <= bloques:
            niveles = niveles + 1
            bloques_sobrantes = bloques_por_nivel

    # triangulo con espacios por nivel
    for i in range(niveles):
        num_espacio = niveles - 1
        print(' ' * (num_espacio - i) + '* ' * (i + 1))

    # Bloques que sobran
    bloques_sobrantes = bloques - bloques_sobrantes
    # Esto solo funciona en python 3
    print(f'\nDe {bloques} bloque/s sobro {bloques_sobrantes} bloque/s')


# -------------------------------------------------------------------------

# Menu
print('<<¡BIEVENIDO!>>')
while True:
    print('----------------------------------------------------------')
    print('<<MENU>>')
    print('1-Determina si un numero entero es primo.\n'
          '2-Niveles de una piramide por el numero de bloques.\n'
          '\nSalir: Presione cualquier tecla para salir.\n')
    try:
        opcion = int(input('Elije una opcion: '))
        print('----------------------------------------------------------')
    except:
        print('----------------------------------------------------------')
        print('<<¡ADIOS!>>')
        break

    if opcion == 1:
        try:
            numero = int(input('Introduzca un numero para verificar si es primo: '))
            primo(numero)
        except:
            print("¡Valor no valido!")

    elif opcion == 2:
        print('Piramide en proceso')
        try:
            bloques_ingresados = int(input('Introduzca el numero de bloques que desea: '))
            print('')
            if bloques_ingresados >= 0:
                piramide(bloques_ingresados)
            else:
                print('¡Valor no valido!')
        except:
            print("¡Valor no valido!")

    else:
        print('<<¡ADIOS!>>')
        break

    print('')
