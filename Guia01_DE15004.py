#numero primo
print('Numeros primos')
x = int(input('Ingresa el numero1: '))
def Numero_primo(numero):
    if numero < 2:
        return False
    elif numero == 2:
        return True
    else:
        for i in range(2, numero):
            if numero % i == 0:
                return False
        return True


resultado = Numero_primo(x)
if resultado is True:
    print('El numero es primo')
else:
    print('El numero no es primo')


# MCD
print("\n")
print("2. Maximo Común Divisor")


def mcd(a, b):
    resto = 0
    while (b > 0):
        resto = b
        b = a % b
        a = resto
    return a


num1 = int(input("Introduzca el primer numero: "))
num2 = int(input("Introduzca el segundo numero: "))

print("El máximo común divisor de ", num1, " y ", num2, " es ", mcd(num1, num2))


