#Guia 1 SAUL ALFREDO LOPEZ MARTINEZ LM12002#
while True:
    try:
        n = int(input("Ingrese numero para convertirlo a binario: "))
        print(format(n, "0b"))
    except ValueError:
        print("Debes escribir un número.")
        continue

    if n < 0:
        print("Debes escribir un número positivo.")
        continue
    else:
        break

