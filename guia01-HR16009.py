#Variable de opcion para el menu
int_op: int = 1
#menu  de eleccion de ejercicios programados
while 0 < int_op <= 2:
    try:
        opcion = input("Ingrese la opcíon deseada \n  1. Conversor de decimal a binario. \n\
        2.Ejercicio de numeros primos. \n Ingrese 0 o cualquier otro numero para salir\n")
        int_op = int(opcion)
    except:
        print("Error...Ingrese solo numeros enteros")
        continue
#opcion 1 de conversor decimal a binario
    if int_op == 1:
        print("opcion 1")
        decimal = input("Ingrese el numero decimal para convertir a binario:   ")
        d = int(decimal)
        cadena = ""
        siguiente_dividendo = d
        while siguiente_dividendo > 1:
            resultado = siguiente_dividendo % 2
            siguiente_dividendo = siguiente_dividendo // 2

            cadena = str(resultado) + cadena
        cadena = str(siguiente_dividendo) + cadena
        print(cadena)

    elif int_op == 2:
        print('opcion 2')

        N = input("Ingrese el numero para verificar si es primo:   ")
        np = int(N)
        contador = 0
        for divisor in range(1, np - 1):
            x = np % divisor
            if x == 0:
                contador = contador + 1

        if contador == 1:
            print("El numero que ingreso es primo \n \n")
        else:
            print("El numero que ingreso no es primo \n \n")

    else:
        print("ADIOS")
