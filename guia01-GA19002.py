excepcion=True
condicion=True
div=2
print("***Numero primo***")
while(excepcion):
    try:
        numero=int(input("ingrese un numero entero para saber si es primo:\n"))
        excepcion=False
    except:
        print("el valor que ingreso no es un entero")

while (condicion):
    if (numero%div==0 and div <numero):
        print(f"El numero: '{numero}' No es un numero primo\n")
        condicion = False
    elif (numero%div==0 and numero==div):
        print(f"El numero: '{numero}' es un numero primo\n")
        condicion=False
    else:
        div = div + 1


lista=[]
cuenta=["primer","segundo","tercer"]
i=0
print("***Meidana de 3 numeros***")
print("Ingrese 3 nuemros para saber su mediana")
while(i<=2):
    excepcion2 = True
    while (excepcion2):
        try:
            numero2=int(input(f"Ingrese el {cuenta[i]} numero entero:\n"))
            excepcion2=False
        except:
            print("el valor que ingreso no es un entero")
    lista.append(numero2)
    i=i+1

lista.sort()
print(f"La mediana de los 3 numeros '{lista}' es: {lista[1]}\n")



excepcion3=True
print("***Convertir numeros decimales a binarios***")
while (excepcion3):
    try:
        numero3 = int(input("Ingrese el numero entero:\n"))
        excepcion3 = False
    except:
        print("el valor que ingreso no es un numero entero")

print(f"El numero binario de {numero3} es:\n {bin(numero3)}")

