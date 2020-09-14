#Determina si un numero es primo o no

numero = int(input("Ingrese el numero: "))
contador=0

for valor in range (1, numero+1):
    if numero % valor ==0:
                contador= contador+1
if contador==2:
    print(f"El numero {numero} es primo")
else:
    print(f"El numero {numero} no es primo")
