#Primos
print("1- Numeros Primos")
a= int(input("Introduce un número para verificar si es primo: "))

def es_primo(num):
    contador=0

    for i in range(1,num+1):
        if num % i==0:
            contador=contador+1

    if contador==2:
        return True
    else:
        return False

resultado = es_primo(a)
if resultado is True:
    print('El numero es primo')
else:
    print('El numero no es primo')
#MCD
print("\n")
print("2- Maximo Común Divisor")
def mcd(a, b):
    resto = 0
    while (b > 0):
        resto = b
        b = a % b
        a = resto
    return a

num1 = int(input("Introduce el primer numero: "))
num2 = int(input("Introduce el segundo numero: "))

print("El máximo común divisor de ", num1, " y ", num2, " es ", mcd(num1, num2))