##Piramide
print("Ejercicio de la piramide\n")
a = int(input("Ingrese el numero de la bloques : \n"))
contador = 0

bloquesPuestos = int(a)
for i in range(1, a):
    if bloquesPuestos < i:
        if bloquesPuestos > 0:
            print(f"Le han sobrado {bloquesPuestos} bloques")
        else:
            print("Le han quedado 0 bloques")
        break
    else:
        bloquesPuestos = bloquesPuestos - i
        print(' ' * (a - i), '* ' * (i))


##Mediana
print("Ejercicio de la mediana\n")
a = float(input("Ingrese el primer valor :"))
b = float(input("Ingrese el segundo valor :"))
c = float(input("Ingrese el tercer valor :"))
d = (a+b+c)/3

print("La mediana es :",float(d))
