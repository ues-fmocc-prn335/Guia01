try:
    menu=int(input("Ejercicios\nIngrese el numero 1 o 2 para ver el respectivo programa\n1-Numeros Primos\n2-Niveles de una piramide\n->"))
except:
    #mensaje en dado caso que no haya ingresado un numero correcto
    print("Error en el numero ingresado")
    exit()
if(menu==1 or menu==2):
    if (menu == 1):
        print("Ejercicio 1\n")

        #Inicio del programa para saber si un numero es primo
        #Comenzamos con una validacion por si el usuario no digita un entero
        try:
            num=int(input("Ingrese un numero entero\n->"))

        except:
            print("No es un numero entero")
            exit()
        #luego procedemos a validar si el numero que el usuario digito es positivo

        if (num>=0):
            if num > 1:
                #Contador nos sirve para identificar si el restante de la division que se hara en la linea 25 de codigo para sumarle uno
                #si es que la division se puede realizar
                #Si se puede realizar sumara uno y eso nos dira que no es un primo ya que un primo solo se
                #puede dividir entre uno y el mismo es por eso que en el rago solo ocuapos desde 2 hasta un numero menos que el digite
                contador = 0
                for i in range(2, num):
                    restante = num % i

                    if restante == 0:
                        contador = contador + 1
                if contador == 0:
                    print("El {} es un numero primo".format(num))
                else:
                    print("El {} no es un numero primo".format(num))
            else:
                print("El {} no es un numero primo".format(num))
        else:
            print("El numero tiene que ser entero positivo")
            exit()

            ## Fin del ejercicio del numero primo


    else:
        print("Ejercicio 2\n")
        ##Inicio del programa de los niveles de una piramide
        bloquestotales = 0
        numerorestador = 1
        nbloques = 0
        nescalones = 0
        sobrante = 0

        # Ingresar la cantidad de bloques que el usuario desea
        try:
            numerodebloques = int(input("Ingrese el numero de bloques que desee en la piramide(Tiene que ser un entero positivo)\n-> "))

        except:
            print("Dato no valido")
            exit()

        # En dado caso de que el numero de bloques sea 0, 1 o 2 se le dira que no es posible crear una piramide con tan poco bloques
        if (numerodebloques == 0 or numerodebloques == 1 or numerodebloques == 2):
            print("No es posible hacer una piramide con esos numeros de bloques")
            exit()
        # En dado caso de que el usuario digite un numero que sea menor a 0 se le advertira de que no se puede hacer una piramide con numeros negativos
        if (numerodebloques < 0):
            print("No se puede hacer una piramide con numeros negativos")
            exit()
        nbloques = numerodebloques

        # Una vez los bloques sean mayor a 2 procedemos a encontrar cuantos escalones tendra la piramide
        #
        # nbloques lo ocuparemos para duplicar la respuesta del usuario para no modificar la cantidad elegida por el usuario
        # nescalones nos servira para conocer cuantos escalones tendra la piramide
        # bloquestotales nos servira para conocer cuantos bloques se ocuparan para construir una piramide
        # numerorestador lo ocuparemos para ir restando desde arriba de la piramide e ir restando hasta conocer cuanto sera los escalones que esta lleva

        for iteracion in range(numerodebloques):
            # ocuparemos este if para saber cuantos bloques se ocuparan para hacer una piramide perfeta
            if (nbloques - numerorestador >= 0):
                nescalones += 1
                bloquestotales = bloquestotales + numerorestador
                nbloques = nbloques - numerorestador
                numerorestador = numerorestador + 1
            else:
                # Si los bloques no alcanzan o justo se terminan para hacer otra fila de bloques el for se dentendra y nos quedaremos con los datos aantes guardados
                break

        print("los bloques que se pueden utilizar son: ", bloquestotales)

        # Este bucle se ocupara para recorrer desde la punta de la piramide hacia abajo e ir imprimiendo esta para dibujarla
        for iteracion in range(nescalones + 1):
            print(" " * (numerorestador), "* " * (iteracion))
            numerorestador = numerorestador - 1
        sobrante = bloquestotales - numerodebloques
        sobrante = sobrante * (-1)
        print("\nLa cantidad de bloques que no se pueden usar son: ", sobrante)

        ##
else:
    print("El numero de ejercicio no existe")
    exit()