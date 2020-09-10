#funciones
def media(valor1, valor2, valor3):
    mediana = ((valor1 + valor2 + valor3) / 3)
    print("la media de los valores agregados es de: "+str(mediana))

def primo(num):
    contador=0
    for i in range (1, num+1):
        if num % i == 0:
            contador= contador+1
    if contador==2:
        print("El número "+ str(num)+ " es un numero primo")
    else:
        print("El número " + str(num) + " no es un numero primo")

#Un pequeño menú
print("Ingrese un valor para la función que quiere realizar")
opcion = int(input("Obtener la media de 3 valores---presione 1" + "\n" + "Determinar si un número es primo---presione 2"+ "\n"))

if opcion == 1:
    dato1 = int(input("Ingrese un primer número: "))
    dato2 = int(input("Ingrese un segundo número: "))
    dato3 = int(input("Ingrese un segundo número: "))
    media(dato1, dato2, dato3)

    decision=int(input("Desea probar el otro codigo?---oprima 1 para determinar si un número es primo"+ "\n"))

    if decision == 1:
        cantidad=int(input("Ingrese un numero (positivo)"))
        if cantidad<=0:
            print("El numero que ingresó es menor o igual a 0"+ "\n"+"por lo tanto no se descubrirá si es primo o par")
        else:
            primo(cantidad)
    else:
        print("hasta la proxima :)")
elif opcion == 2:
        cantidad = int(input("Ingrese un numero (positivo): "))
        if cantidad <= 0:
            print("El numero que ingresó es menor o igual a 0" + "\n" + "por lo tanto no se descubrirá si es primo o par")
            decision = int(input("Desea probar el otro codigo?---oprima 1 para determinar la media de 3 numeros" + "\n"))

            if decision == 1:
                dato1 = int(input("Ingrese un primer número: "))
                dato2 = int(input("Ingrese un segundo número: "))
                dato3 = int(input("Ingrese un segundo número: "))
                media(dato1, dato2, dato3)
            else:
                print("hasta la proxima :)")
        else:
            primo(cantidad)
            decision=int(input("Desea probar el otro codigo?---oprima 1 para determinar la media de 3 numeros"+ "\n"))

            if decision == 1:
                dato1 = int(input("Ingrese un primer número: "))
                dato2 = int(input("Ingrese un segundo número: "))
                dato3 = int(input("Ingrese un segundo número: "))
                media(dato1, dato2, dato3)
            else:
                print("hasta la proxima :)")