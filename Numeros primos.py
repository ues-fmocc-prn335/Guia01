num = int(input("Ingrese el numero: "))
numPrimo = True
for i in range(2, num):
   if num % i == 0:
     numPrimo = False
     break

if numPrimo==True:
    print("El numero ",num," es primo")
else:
    print("El numero ", num, " no es primo")