import math

def esPrimo(num):
    if num < 1:
        return False
    elif num == 2:
        return True
    else:
        for i in range(2, num):
            if num % i == 0:
                return False
        return True

def binario(decimal):
    binario = ''
    while decimal // 2 != 0:
        binario = str(decimal % 2) + binario
        decimal = decimal // 2
    return str(decimal) + binario

def piramide(bloques):
    fila=0
    bloque=int(math.sqrt(bloques))
    for i in range(1, bloque+1):
        fila +=2
        for j in range(bloques-i):
            print (" ",end="")
        for k in range(i,fila):
            print ("#",end="")
        for l in range(fila-2,i-1,-1):
            print ("#",end="")
        print()
    return



def app():
    opcion=1
    while opcion == 1 :
        print("------------------MENÚ------------------")
        print("1: Probar si un número entero es Primo")
        print("2: Convertir un número decimal a binario")
        print("3: Realizar una piramide ingresando el numero de bloques")
        print("0: Salir del programa")
        print("----------------------------------------")
        try:
            opcion = int(input("Ingrese una opcion a realizar: "))
        except:
            print("Dato incorrecto: Introduzca una opcion numerica")
            continue

        if opcion==1 :
            num=0
            while num<1 :
                try:
                    num = int(input('Ingrese un número entero: '))
                except:
                    print("Dato incorrecto: Introduzca un digito")
                    continue
            result = esPrimo(num)
            if result is True:
                print('El número ES Primo')
            else:
                print('El número NO ES Primo')
            opcion=0

        elif opcion==2 :
            decimal = 0
            while decimal < 1:
                try:
                    decimal = int(input('Ingrese un número decimal para convertir a binario: '))
                except:
                    print("Dato incorrecto: Introduzca un digito")
                    continue
            resultado = binario(decimal)
            print("El resultado de", decimal, " en binario es:", resultado)

        elif opcion == 3 :
            bloques = 0
            while bloques < 1 or bloques > 100:
                try:
                    bloques = int(input('Ingrese el número de bloques que desea (1-100): '))
                except:
                    print("Dato incorrecto: Introduzca un digito")
                    continue
            resul=piramide(bloques)
            print(resul)

        elif opcion==0 :
            break

        else :
            print("Dato incorrecto: Ingrese una opción correccta")
            opcion=1

if __name__ == '__main__':
    app()
