#Ejerecicios GUIA01 PROGRAMACION III

#Determinar si un numero entero es “Primo”
#Conversor de decimal a binario

try:
    operaciones = int(input("Seleccione una operacion. \n1.Numero primo.\n2.Conversor de decimal a binario.\nSeleccion: "))
except:
    print("Opcion invalida")
    quit()

#Numero Primo
def es_primo(numero):
    contador = 0

    for i in range(1, numero+1):
        if numero % i == 0:
            contador += 1

    if (contador ==2 ):
        print("El numero ", numero, " es primo")
        quit()
    else:
        print("El numero ", numero, " No es primo")
        quit()

#Decimal a Binario
def decimal_binario(decimal):
    binario=''
    while decimal // 2 != 0:
        binario=str(decimal%2)+binario
        decimal=decimal // 2
    return str(decimal)+binario


#Operacion segun seleccion

if (operaciones == 1):
    try:
        numero = int(input("Digite un numero para determinar si es primo o no: "))
        es_primo(numero)
    except:
        print("Error: Dato no valido")
        quit()

if (operaciones == 2):
    try:
        numero = int(input('Introduce el número a convertir a binario: '))
        print("El numero ",numero," a binarios es ",decimal_binario(numero))
    except:
        print("Error: Dato no valido")
        quit()