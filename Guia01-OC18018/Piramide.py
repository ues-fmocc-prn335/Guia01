#OC18018-Osorio Clemente,José Armando

#validar errores de ingreso
try:
    #Cuadros que ingresara el usuario
    cuadros=int(input("Ingrese la cantidad de cuadros que desea dibujar"))
    bandera=True
    #Validar si se puede crear la piramide
    if cuadros>2:
        #for para obtener a base
        for b in range(cuadros):
            #Validacion de piramide normal
            if (b * (b + 1) / 2) == cuadros:
                print('la base es ', b)
                for i in range(1, b + 1):
                    print(" " * (b - i), end="")
                    print(" *" * i)
                bandera = False
            #Valida si es una piramide donde sobran cuadros
            elif (b * (b + 1) / 2) > cuadros and bandera == True:
                print('la base es ', b)
                contador =0
                for i in range(1, b):
                    print(" " * (b - i), end="")
                    print(" *" * i)
                    contador=contador+i
                print("Los cuadros que sobran son",cuadros - contador)
                break
    else:
        print("No es posible crear una piramide, el valor ingresado debe ser mayor a 2")
except ValueError as e:
    print("ERROR: ",e)