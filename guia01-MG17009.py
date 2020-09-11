#Saber si un numero es primo
print('Numeros primos')
x = int(input('Ingrese el valor: '))
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

#MCD de dos numeros
def MCD(a, b):
    resto = 0
    while (b > 0):
        resto = b
        b = a % b
        a = resto
    return a
print('Maximo comun divisor')
num1 = int(input("Introduce el primer numero: "))
num2 = int(input("Introduce el segundo numero: "))

print("El máximo común divisor de ", num1, " y ", num2, " es ", MCD(num1, num2))