# Nombre de usuario en GitHub:  Ivan9962
def mcd(a, b):
	resto = 0
	while (b > 0):
		resto = b
		b = a % b
		a = resto
	return a



num1 = int(input("Introduce el primer numero: "))
num2 = int(input("Introduce el segundo numero: "))

print("El maximo comun divisor de ", num1, " y ", num2, " es: ", mcd(num1, num2))