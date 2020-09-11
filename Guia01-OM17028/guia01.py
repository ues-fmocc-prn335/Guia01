def piramide():

    try:
        n = int(input('ingrese el numero de bloques a usar '))
    except:
        print("Error tiene que ingresar un numero entero de bloques ")
        exit()

    if n == 1 or n == 2 or n <= 0:
        print("no se puede hacer una piramide con", n, "numeros de bloques")
        exit()
    space = 1
    flag = True

    for base in range(n):

        if (base * (base + 1) / 2) == n:

            for i in range(1, base + 1):
                print(" " * (base - space), "* " * (i))
                space = space + 1
            flag = False


        elif (base * (base + 1) / 2) > n and flag == True:
            sobrante = 0

            for i in range(1, base):
                print(" " * (base - space), "* " * (i))
                space = space + 1
                sobrante = sobrante + i

            print("no se puede hacer una piramide con", n, "numero de bloques\nEl numero de bloques que sobran son ",
                  (n - sobrante))
            break

def binario(decimal):
    binario = ''
    while decimal // 2 != 0:
        binario = str(decimal % 2) + binario
        decimal = decimal // 2

    return print(str(decimal) + binario)

option=int(input("Que desea hacer\n1.piramide\n2.convertir a binario\nCualquier otro numero para salir\t"))
while option==1 or option==2:
    if(option==1):
        piramide()
    else:
        binario(int(input("ingrese el numero \t")))
    option = int(input("\n\n\nQue desea hacer\n1.piramide\n2.convertir a binario\nCualquier otro numero para salir\t"))
