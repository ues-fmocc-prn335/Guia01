##Autor: Giovanni Aguirre AH19022

def validarEntero(entrada):
 
   while True: 
       try:
           entrada = int(entrada)
           return True
       except ValueError:
           print("\nEntrada erronea, por favor digite un numero entero\n")
           return False


def validarMenu():
    opcionvalida=False
    while opcionvalida==False:
        numeroentrada=input("\n\nMenu :)\n1- Conversor binario a decimal \n2- Determina si un numero es primo\n3-Salir ")
        if validarEntero(numeroentrada):
            opcionvalida=True
            numeroentrada= int(numeroentrada)
            return numeroentrada
        else:
            print("\nPor favor digite un numero valido.\n")
    
def determinarSiEsPrimo(numero):
  
    numero = int(numero)
    contadorDeDivisores = 0

    for x in range(1,numero+1):
        if (numero%x)==0:
            contadorDeDivisores=contadorDeDivisores+1

    if contadorDeDivisores==2:
        print("si es un numero primo")
    else:
        print("no es un numero primo")            

def conversorDecimalBinario(numeroaConvertir):
    
    numeroaConvertir=int(numeroaConvertir)
    resultado=""

    while numeroaConvertir != 0:
        residuo = numeroaConvertir % 2
        numeroaConvertir = numeroaConvertir // 2
        resultado = str(residuo) + resultado

    print("El numero convertido a binario es: ", resultado)


opcion = validarMenu

while opcion != 0:
    if (opcion == 1):
        numeroentrada=input("Digite el numero a convertir a binario: ")
        if validarEntero(numeroentrada):
             conversorDecimalBinario(numeroentrada)
        else:
             print("\nPor favor digite un numero valido.\n")
	    
    elif(opcion ==2):
        numeroentrada=input("Digite un numero entero para determinar si es un numero primo: ")
        if validarEntero(numeroentrada):
             determinarSiEsPrimo(numeroentrada)
        else:
             print("\nPor favor digite un numero valido.\n")
	    
    else:
	    print("\nDigite una opcion valida del menu.\n")


    opcion = validarMenu()
