#Centrar texto
frase=input("Escriba una frase o palabra\n").upper()
print(frase.center(160," "))


#Encontrar la mediana
num1 = input("Escribe el primer nùmero:\n")
num2 = input("Escribe el segundo nùmero:\n")
num3 = input("Escribe el tercero nùmero:\n")
lista = [int(num1), int(num2), int(num3)]
lista.sort()
print(f"La mediana es:  {lista[1]}")


#conversor de dedcimal a binario
numero = input("Escribe el numero que quieres convertir:\n")

print("{0:#b}".format(int(numero)).replace("b",""))
