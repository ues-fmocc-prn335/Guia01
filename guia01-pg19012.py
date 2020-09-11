def binario():
    binario = ''
    while True:
        try:
            decimal = int(input('Ingrese el numero que quiere convertir: '))
            break
        except ValueError:
            print("Ingrese numeros")

    while decimal // 2 != 0:
        binario = str(decimal % 2) + binario
        decimal = decimal // 2
    return str(decimal) + binario
def mediana():
    while True:
        try:
            a = int(input("Ingrese primer numero:"))
            b = int(input("Ingrese Segundo numero:"))
            c = int(input("Ingrese Segundo numero:"))
            break
        except ValueError:
            print("Ingrese numeros")

    lista=[a,b,c]
    lista.sort()
    print("La mediana es: ",lista[1])
def primo():
    while True:
        try:
            numero = int(input("Ingrese numero para verificar si es primo"))
            break
        except ValueError:
            print("Ingrese numeros entero")

    contador = 0
    for i in range(1, numero + 1):
        if (numero % i) == 0:
            contador = contador + 1

    if contador == 2:
        print("El numero(", numero ,")es primo")
    else:
        print("El numero(",numero,") no es primo")

def mcd():

    while True:
        try:
            a=int(input("Ingrese primer munero:"))
            b=int(input("Ingrese segundo numero:"))
            break
        except ValueError:
            print("Ingrese numeros")


    mcd=1
    if a%b==0:
        print(b)
    for k in range(int(b/2),0,-1):
        if (a%k==0) and (b%k==0):
           mcd=k
           break
    print(mcd)

def centrar():
    frase=input("Ingrese una palabra, frase o numeros")
    print(frase.center(40,"="))

'''def piramide():

        casillas = int(input("Ingrese numero de casillas"))
        for i in range (casillas):
            print("*"*i)'''




while True:
  while True:

    while True:
        try:
            programa = int(input(
                "\nPor favor Ingrese El numero de la funcion que quiere\n1)Convertir de decimal a binario\n2)Sacar la mediana de 3 numeros\n3)Saber si es primo\n4)Sacar maximo comun divisor\n5)Centrar\n6)Salir\nNumero:"))

            break
        except ValueError:
            print("Ingrese numeros")

    if (programa>0)and(programa<=6):
        break

  if(programa==1):

    print(binario())
  elif(programa==2):
    mediana()
  elif(programa==3):
      primo()
  elif(programa==4):
      mcd()
  elif(programa==5):
      centrar()
  elif(programa==6):
      quit()
  #elif(programa==7):
  #    quit()