#primos

def numerosprimos(n):
    if n<2:
        return False

    for x in range(2,n):
        if n%x==0:
            return False

    return True

n = int(input("ingrese un numero: "))
if numerosprimos(n) is True:
    print("El numero ",n ,"es un numero primo")

else:
    print("el numero ",n,"no es primo")


print("Fin de numeros primos \n\n")

#binario_a_decimal
def dec_bin(decimal):
    resultado = ""
    while decimal>0:
        residuo = decimal%2
        resultado=resultado+str(residuo)
        decimal=decimal//2

    return resultado[::-1]


numero=int(input("ingrese un numero "))
print(dec_bin(numero))