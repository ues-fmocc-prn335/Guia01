# ----------------------------------------------------------------
# **********    UNIVERSIDAD DE EL SALVADOR - PG18037    **********
# ----------------------------------------------------------------

# ----------------------------------------------------------------
# **********    EJERCICIO DE LA MEDIANA DE 3 NUMEROS    **********
# ----------------------------------------------------------------
def mediana():
    numero1 = int(input('Ingrese el primer numero\n'))
    numero2 = int(input('Ingrese el segundo numero\n'))
    numero3 = int(input('Ingrese el tercer numero\n'))

    if numero1 > numero2 and numero1 > numero3:
        if numero2 > numero3:
            print("La mediana es el numero", numero2)
        else:
            print("La mediana es el numero", numero3)
    elif numero2 > numero1 and numero2 > numero3:
        if numero1 > numero3:
            print("la mediana es el numero ", numero1)
        else:
            print("La mediana es el numero", numero3)
    elif numero3 > numero1 and numero3 > numero2:
        if numero1 > numero2:
            print("La mediana es el numero", numero1)
        else:
            print("La mediana ees el numero", numero2)
    elif numero1 == numero2:
        print("La mediana es ", numero1)
    elif numero2 == numero3:
        print("La mediana es ", numero2)
# ----------------------------------------------------------------------------
# **********    EJERCICIO PARA DETERMINAR SI UN NUMERO ES PRIMO     **********
# ----------------------------------------------------------------------------
def primos():
    primo = int(input("Ingrese un numero\n"))
    esprimo = True
    count = 0

    for i in range(primo):
        result = primo%(i+1)
        if result == 0:
            print(primo, "%", (i+1)," = ", result)
            count = count+1
            if count > 2:
                esprimo = False
                break
        else:
            print(primo, "%", (i+1)," = ", primo/(i+1))

    if esprimo:
        print("\nES PRIMO!")
    else:
        print("\nNO ES PRIMO :c")

# ----------------------------------------------------------------------------
# **********    ESCOGE EL EJERICIO QUE QUIERES CORRER o LOS DOS     **********
# ----------------------------------------------------------------------------
mediana()
# primos()