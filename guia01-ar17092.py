#Método para selecciónar las funciones que el usuario desee
def menu():

    #Para tener un menu interactivo haremos uso de un buce while
    while True:

        #Validamos si el usuario ingreso un dato erroneo, para ello utilizamos un try-except
        #Si el error lo atrapa seguiremos con el codigo del script con un continue
        try:
            opcion=int(input("\nIngrese el número de la opción:\n"+
                            "1. Comprobar si un numero es primo.\n"+
                            "2. Convertir número decimal a binario.\n"+
                            "3. Salir. -->| "))
        except:
            print("\nError. Has ingresado una letra o simbolo, en lugar de un número.\n")
            continue
        

        #Validamos según lo que el usuario a seleccionado con unas condiciones básicas
        #Volvemos a hacer uso de try-except por si el usuario comete un error al ingresar datos
        if opcion == 1:
            try:
                num=int(input("\nIngrese el número a comprobar.\n"))
            except:
                print("\nError. Has ingresado una letra o simbolo, en lugar de un número.\n")
                continue

            #Llamamos al método que creamos para comprobar si un número es primo o no
            #En este caso no hay necesidad de importar modulo, ya que la funcion
            #esta dentro del mismo script
            numPrimo(num)
        elif opcion == 2:
            try:
                num=int(input("\nIngrese el número a comprobar.\n"))
            except:
                print("\nError. Has ingresado una letra o simbolo, en lugar de un número.\n")
                continue
            
            #Llamamos al método que creamos para convertir un número decimal a binario
            #En este caso no hay necesidad de importar modulo, ya que la funcion
            #Esta dentro del mismo script
            converter(num)
        else:

            #si el usuario no desea nada de lo ofrecido podrá cerrar el script con la opcion 3
            #Utilizamos un break, debido a que la condicion del bucle siempre será cierta
            #Con break podemos terminar los procesos
            if opcion == 3:
                break
            
            #Si el usuario ingresa una opcion que no existe se le imprimirá un mensaje por pantalla
            #Y volvera al ciclo(menú)
            elif opcion != 1 or opcion != 2 or opcion != 3:
                print("\nEsa opción no existe, selecione una opción correcta.\n")

#Método para conprobar si un número es primo.
def numPrimo(num):
    #No podemos tomar encuenta el uno por eso lo descartamos al principio
    if num == 1:
        print("\n",num," no se toma en cuenta.\n")
    else:
        #inciamos un contador, ya que esto nos ayudará para las líneas de código más adelante
        count = 0;

        #En un bucle for con repeticiones en un rango de el número ingresado
        #Pondremos una condición y cada vez que el modulo % nos regrese un 0
        #aumentaremos el contador
        for i in range(1,num+1):
            if num%i == 0:
                count +=1

        #Dependiendo de las veces que se aumento el contador podremos ver
        #si es primo, logrando esto con las reglas existentes
        #
        
        
        if count == 2:
            print("\n",num," es un número primo\n")
        else:
            print("\n",num,"es un número compuesto\n")

#Método para convertir un número decimal a binario
def converter(decimal):
    #Definimos una lista vacía para almacenar todo el número binario que obtendremos
    binario=list()

    if decimal == 0:
        print("\n",decimal," base 10 = 0 base 2\n")
    elif decimal == 1:
        print("\n",decimal," base 10 = 1 base 2\n")
    else:
        decimalO=decimal

        #Declaramos una variable @cociente para almacenar el cociente, este tiene que ser entero para poder
        #hacer la conversión de decimal a binario
        cociente=None

        #Trabajamos con while para realizar las divisiones necesarias hasta alcanzar los datos que necesitamos
        #para terminar la conversión
        while cociente != 1:

            #'''Hacemos uso del modulo % para despues guardar el residuo entre el numero a convertir y 2 en una variable @mod'''
            mod = decimal%2
            
            #'''Hacemos cast de la division por si el número es flotante así también impedimos que este se aproxime'''
            cociente= int(decimal/2)

            #'''Como el cociente puede ser mayor a 1 en estas condiciones, le decimos que almacene un valor(1) en la lista ya creada
            #por las reglas que deben cumplir los numeros de base 2'''
            if mod == 0 or mod == 1 :
                binario.append(mod)
            elif mod > 1:
                binario.append(1)
            decimal=cociente

       # '''Debido a la condición del bucle añadimos el ultimo valor a la lista para así tener la conversión completa '''    
        binario.append(cociente)
    
    #'''Imprimimos la lista a la cual fueron añadidos los residuos y el cociente final, para ello ocupamos un for, y utilizamos el metodo reversed'''
    numeroBinario= list()

    for i in reversed(binario):
        numeroBinario.append(i)
    print("\n",decimalO," base 10 = ",numeroBinario," base 2\n")

print("¡Hola!\n")
menu()