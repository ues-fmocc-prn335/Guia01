

def numerosPrimos():
    bo2 = 1
    while bo2:
        bo1 = 1
        v3 = input("1.ver si un numero es primo\n2.obtener numeros primos\n escriba \"salir\" para salir\n")
        if v3.lower() == "salir":
            bo2 = 0
        else:
            try:
                v4 = int(v3)
            except:
                print("ingrese \"1\", \"2\" o \"salir\"\n")
                continue
            if v4 == 1:
                while bo1:
                    v1 = input("ingrese el numero que desea probar\n")
                    try:
                        v2 = int(v1)
                    except:
                        print("favor escribir un numero\n")
                        continue
                    if v2 < 2:
                        print("ingrese un valor igual o mayor a 2\n")
                        continue
                    cont1 = 2
                    while bo1:
                        if v2 == cont1:
                            print("es primo\n")
                            bo1 = 0
                        elif v2 % cont1 == 0:
                            print("no es primo\n")
                            bo1 = 0
                        else:
                            cont1 = cont1 + 1

            elif v4 == 2:
                while bo1:
                    v1 = input("ingrese el numero de numeros primos que desea ver\n")
                    try:
                        v2 = int(v1)
                    except:
                        print("favor escribir un numero\n")
                        continue
                    if v2 < 1:
                        print("ingrese un valor igual o mayor a 1\n")
                        continue
                    cont1 = 2
                    cont2 = 2
                    cont3 = 0
                    while bo1:
                        if v2 == cont3:
                            bo1 = 0
                        elif cont1 == cont2:
                            cont3 = cont3 + 1
                            print("N°" + str(cont3), cont1)
                            cont1 = cont1 + 1
                            cont2 = 2
                        elif cont1 % cont2 == 0:
                            cont1 = cont1 + 1
                            cont2 = 2
                        else:
                            cont2 = cont2 + 1
            elif v4 != 1 and v4 != 2:
                print("ingrese un \"1\" o \"2\"\n")
                continue
def sumGaus(v1):
    bo1 = 1
    c1 = 0.0
    while bo1:
        if (c1 * (c1 + 1)) / 2 > v1:
            bo1 = 0
            c1 = c1 - 1
        else:
            c1 = c1 + 1
    return c1
def piramideCompleta(v2):
    pi1 = sumGaus(v2)
    cont1 = 0
    bo1 = 1
    while bo1:
        print(" " * int(pi1 - cont1) + "* " * int(cont1 + 1))
        cont1 = cont1 + 1
        if cont1 == pi1:
            print("la piramide tiene " + str(int(pi1)) + " niveles\n y esta echa con " + str(int((pi1 * (pi1 + 1)) / 2)) + " bloques\n sobran " + str(int(v2 % ((pi1 * (pi1 + 1)) / 2))) + " bloques\n")
            return  0

def piramide():
    bo2 = 1
    while bo2:
        bo1 = 1
        v1 = input("1.ver piramide de arriba hacia abajo\n2.piramide de abajo arriba\nescriba \"salir\" para salir\n")
        if v1.lower() == "salir":
            bo2 = 0
        else:
            try:
                v2 = int(v1)
            except:
                print("favor escribir un numero\n")
                continue
            if v2 == 1:
                while bo1:
                    v1 = input("ingrese el numero de bloques que formaran la piramide\n")
                    try:
                        v2 = int(v1)
                    except:
                        print("favor escribir un numero\n")
                        continue
                    if v2 < 1:
                        print("ingrese un valor igual o mayor a 1\n")
                        continue
                    bo1 = piramideCompleta(v2)
            elif v2 == 2:
                while bo1:
                    v1 = input("ingrese el numero de bloques que formaran la piramide\n")
                    try:
                        v2 = int(v1)
                    except:
                        print("favor escribir un numero\n")
                        continue
                    if v2 < 1:
                        print("ingrese un valor igual o mayor a 1\n")
                        continue
                    pi1 = sumGaus(v2) + 1
                    if (pi1 * (pi1 - 1)) / 2 != v2:
                        pi2 = sumGaus((pi1 * (pi1 + 1)) / 2 - v2)
                        cont1 = 0
                        cont2 = 0
                        v3 = (pi1 * (pi1 + 1)) / 2 - v2 - (pi2 * (pi2 + 1)) / 2
                        while bo1:
                            if cont1 < pi2:
                                print("")
                                cont1 = cont1 + 1
                            elif cont1 == pi2 and v3 != 0:
                                print(" " * int(pi1 - cont1) + "  " * int(v3) + "* " * int(pi2 + 1 - v3) + "")
                                cont1 = cont1 + 1
                                cont2 = cont2 + 1
                            else:
                                print(" " * int(pi1 - cont1) + "* " * int(cont1 + 1) + "")
                                cont1 = cont1 + 1
                                cont2 = cont2 + 1
                            if cont1 == pi1:
                                bo1 = 0
                                print("la piramide tiene " + str(int(cont2)) + " niveles\n y esta echa con " + str(
                                    int(v2)) + " bloques\n faltan " + str(
                                    int(v3 + (pi2 * (pi2 + 1)) / 2)) + " bloques para los " + str(
                                    int(pi1)) + " niveles\n")
                    else:
                        bo1 = piramideCompleta(pi1)
            else:
                print("excriba 1 o 2\n")
                continue
bo1 = 1
while bo1:
    x1 = input("\n\nTAREA_2_OG13002\n1.numeros primos\n2.piramides\nescribir \"salir\" para salir\n")
    if "salir" == x1.lower():
        bo1 = 0
    else:
        try:
            x2 = int(x1)
        except:
            print("ingrese \"1\", \"2\" o \"salir\"\n")
            continue
        if x2 == 1:
            numerosPrimos()
        elif x2 == 2:
            piramide()
        elif x2 != 1 and x2 != 2:
            print("ingrese un \"1\" o \"2\"\n")
            continue


