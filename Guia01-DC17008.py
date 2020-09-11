# Guia de programacion lll 01

# primero crearemos un menu para que el usuario eliga el ejercicio que desea

try:
    opciones = int(input(
        "Menú de ejercicios\n1.Numero Primo\n2.Piramide\n#.cualquier tecla para salir\nIngrese el numero de la operacion que desea realizar: "))

except:
    quit()


# Funcion piramide
def piramide(bloques):
    contador = 0
    bloquesPuestos = int(bloques)

    if bloques > 0:

        for i in range(1, bloques):
            if bloquesPuestos < i:
                if bloquesPuestos > 0:
                    print(f"Le han sobrado {bloquesPuestos} bloques")
                else:
                    print("Le han quedado 0 bloques")
                break
            else:
                bloquesPuestos = bloquesPuestos - i
                print(' ' * (bloques - i), '* ' * i)

    else:
        print("El numero tiene que ser mayor a 0")


# Funcion numero primo
def NPrimo(x):
    n = 2
    if x < n:
        print("no es primo")
    else:
        while n < x:
            if x % n == 0:
                print("no es primo")
                break
            n = n + 1
        else:
            print("es primo")

# Menu
if opciones == 1:
    try:
        numero = int(input("Ingrese un numero para determinar si es primo o no: "))
        NPrimo(numero)
    except:
        print("Ingreso un tipo de dato no valido")
        quit()

if opciones == 2:
    try:
        nBloques = int(input("Por favor ingrese el numero de bloques de su piramide: "))
        piramide(nBloques)
    except:
        print("Ingreso un tipo de dato no valido")
        quit()
else:
    print("Fin")
