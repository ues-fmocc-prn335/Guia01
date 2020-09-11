import math

#Centrar texto
print("CENTRAR TEXTO")
frase=input("Escriba una frase o palabra:\n").upper()
print(frase.center(160," "))


#Encontrar la mediana
print("ENCONTRAR LA MEDIANA DE TRES NUMEROS")
num=0
lista = []
while(num<3):
    try:
        numero = int(input("Escribe un nùmero:\n"))
        if(math.isnan(numero) == False):
            lista.append(numero)
            num=num+1
        else:
            print("Debe escribir un numero")
    except:
        print("Debe escribir un numero")
lista.sort()
print(f"La mediana es: {lista[1]}")


#conversor de dedcimal a binario
print("CONVERSOR DE DECIMAL A BINARIO")
validar = False
while(validar==False):
    try:
        numero = int(input("Escribe el numero que quieres convertir:\n"))
        if(math.isnan(numero)==False):
            validar = True
            print("{0:#b}".format(int(numero)).replace("b",""))
        else:
            print("Debe escribir un numero")
    except:
        print("Debe escribir un numero")
