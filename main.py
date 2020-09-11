seleccion=int(input('¿Que desea hacer?\n 1. Ingresar un numero para conocer si es primo\n 2. conocer el binario de un numero\n Ingrese el numero de la opcion deseada\n '))


if seleccion==1:
  print('***DETERMINANDO NUMEROS PRIMOS***')

  numero=int(input('Ingrese un numero entero para determinar si es un numero primo: '))
  contador=0
  if numero<=0:
       while numero<0:
        print('el numero debe ser positivo')
        numero = int(input('Ingrese un numero entero para determinar si es un numero primo: '))


  else:

   print('Usted ha introducido el numero: ',numero)
       #si el numero es 1 o 2, automaticamente se reconoce como primo
  if numero ==1 or numero==2:
      print('El numero', numero, 'es primo')
  else:
    # bucle para realizar divisiones del numero introducido y determinar
    # si es divisible unicamente entre 1 y entre el mismo

    for iter in range(1, numero+1):
     if numero%iter==0:
        contador=contador+1

    if contador==2:
      print('El numero', numero, 'es primo')
    else:
     print('El numero', numero, 'no es un numero primo')


else:
    if seleccion==2:
        print("***CONVERTIDOR DE DECIMAL A BINARIO***\n")

    binario = " "

    numeroDecimal = int(input('Ingrese un numero para convertir a binario '))
    numero = numeroDecimal

    if numeroDecimal < 0:

        print('Debe Ingresar un numero positivo')

    else:
        while numeroDecimal > 0:
            residuo = int(numeroDecimal % 2)
            numeroDecimal = int(numeroDecimal / 2)

            binario = str(residuo) + binario

        print('El numero ', numero, 'en binario es ', binario)



