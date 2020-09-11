#mediana de tres numeros (LG18048)
def calcular_mediana(numero1,numero2,numero3):
    numero1 = int(input("ingrese el primer numero\n"))
    numero2= int(input("ingrese el segundo numero\n"))
    numero3= int(input("ingrese el tercer numero\n"))

    if numero1>numero2:
        if numero1 < numero3:
            return numero1
        elif numero2 > numero3:
            return numero2
        else:
            return numero3
    else:
        if numero1>numero3:
            return numero1

        elif numero2<numero3:
            return numero2

        else:
            return numero3

print("la mediana es ",calcular_mediana(0,0,0))