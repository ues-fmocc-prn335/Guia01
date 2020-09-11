# numero primo (lg18048)
print("se evaluarán los numeros primos")
valido =int
valido = 1
numero=(input("ingrese un numero entero"))
while valido==1:
    try:
        numero=int(numero)
        valido=0
    except:
        print("no ha ingresado un dato valido")
        numero = (input("ingrese un numero entero"))
if numero==1:
    print(f"el numero 1 no es un numero primo")
else:
    if numero == 2:
        print(f"el numero 2  es un numero primo")
    else:
        if numero % 2 == 0:
            print(f"el numero {numero} no es un numero primo")
        if numero % 2 != 0:
            print(f"el numero {numero} es un numero primo")