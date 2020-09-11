

def primo(num):

    cont=0
    if num < 1:
        print("Debe ser mayor a 1")
    elif num ==2:
        print("Es primo")
    else:
            for i in range(2, num):
                if num % i == 0:
                    cont=cont+1


    if cont>0:
        return "No es primo"
    else:
        return "Es primo"


def decimalBinario(decimal):
    binario = ''
    while decimal // 2 != 0:
        binario = str(decimal % 2) + binario
        decimal = decimal // 2
    return str(decimal) + binario


try:
    numero = int(
        input('Introduce el número a convertir a binario \nEl numero que desea convertir de decimal a binario:\n'))
    if numero>0:
        print("Es primo?  R/", primo(numero))
        print("Decimal: " + str(numero) + "\nBinario :", decimalBinario(numero))
except:
    print("Ingrese un numero valido")


