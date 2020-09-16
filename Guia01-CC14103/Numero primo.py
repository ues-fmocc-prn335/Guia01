
# Numero primo
num = int(input("Ingrese un numero : "))
if num > 1:
    contador = 0
    i = 2
    while i< num and contador == 0:
        resto = num % i

        if resto == 0:
            contador += 1
        i+=1

    if contador == 0:
        print("El {} es un número primo".format(num))
    else:
        print("El {} no es un número primo".format(num))

else:
    print("El {} no es un número primo".format(num))
