'''Guia 01 Programacion 3
   Nombre:Bryan Alexander Menendez Samayoa Carnet:MS17015
   1.Numeros primos'''
print("1.Numeros Primos")
def NumeroPrimo(x):

   if(x==1 and x>0):
    print(f"El numero {x} es par \n")
   elif(x%2==1 or x==2 and x>0):
    print(f"El numero {x} es primo \n")
   elif(x%2==0 and x>0):
    print(f"El numero {x}es par \n")
   return " "
while True:
    try:
        numero=int(input("Ingrese un numero \n"))
        break
    except ValueError:
        print("Ingrese numeros enteros \n")
if(numero>0):
  print(NumeroPrimo(numero))
else:
    print("El numero es negativo \n")

'''2.Decimal a Binario'''
print("Convertir de Decimal a Binario")
def decimalbinario(y):
    binario =""
    bin(y)
    binario=int(bin(y)[2:])
    return binario
nDecimal = int(input("Ingrese un numero decimal: \n"))
print(f"El numero {nDecimal} convertido a binario es: {decimalbinario(nDecimal)}")

'''3.Sacar mediana de tres numeros'''
print("Sacar mediana de tres numeros")
def mediana(a, b, c):
    if a > b:
        if a < c:
            return a
        elif b > c:
            return b
        else:
            return c
    else:
        if a > c:
            return a
        elif b < c:
            return b
        else:
            return c


numero1 = int(input("Ingrese el numero 1:"))
numero2 = int(input("Ingrese el numero 2:"))
numero3 = int(input("Ingrese el numero 3:"))
print(f"Le mediana es: {mediana(numero1,numero2,numero3)}")
