#EJERCICIO DE NUMEROS PRIMOS

num = int(input("Ingrese numero:"))
flag = True
for i in range(2, num):
	if not (num % i): flag = False

if flag:
	print("Es primo")
else:
	print("No es primo")

#EJERCICIO DE MAXIMO COMUN DIVISOR

def gcd(a, b):
	if(b == 0):
		return a
	return gcd( b, a % b)

x = int(input("Ingrese primer numero:"))
y = int(input("Ingrese segundo numero:"))

print("El Maximo Comun Divisor de los numeros es " + str(gcd(x, y)))
