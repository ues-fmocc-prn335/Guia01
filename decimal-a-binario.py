binario=""
residuo=0
try:
    numero=int(input("ingrese el numero para calcular su binario\n"))
    if numero<0:
        print("solo numeros positivos")
    else:
        if numero==0:
            print("el binario del numero "+str(numero)+" es: 0")
        else:
            numerooutput=numero
            while numero>=1:
                residuo=numero%2
                binario=str(residuo)+binario
                numero=numero//2
            print("el binario del numero "+str(numerooutput)+" es: "+binario)
except ValueError:
    print("error de dato ingresado")
