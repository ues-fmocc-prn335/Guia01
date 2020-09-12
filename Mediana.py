
def M():
    print("***** Ingrese tres numero para conocer la Mediana *****")
    num1 = int(input('Primer numero\n'))
    num2 = int(input('Segundo numero\n'))
    num3 = int(input('Tercer numero\n'))

    if num1 > num2 and num1 > num3:
        if num2 > num3:
            print("El valor de la mediana es", num2)
        else:
            print("El valor de la mediana es", num3)
    elif num2 > num1 and num2 > num3:
        if num1 > num3:
            print("El valor de la mediana es", num1)
        else:
            print("El valor de la mediana es", num3)
    elif num3 > num1 and num3 > num2:
        if num1 > num2:
            print("El valor de la mediana es", num1)
        else:
            print("El valor de la mediana es", num2)
    elif num1 == num2:
        print("El valor de la mediana es ", num1)
    elif num2 == num3:
        print("El valor de la mediana es ", num2)

M()        
