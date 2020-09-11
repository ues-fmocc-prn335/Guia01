#Números primos
from distlib.compat import raw_input

numero_leido = raw_input("Ingrese un numero: ")
numero = int(numero_leido)
contador = 0
for i in range(1,numero+1):
    if (numero% i)==0:
        contador = contador + 1

if contador==2:
    print("El numero SI es primo")
else:
    print("El numero NO es primo")