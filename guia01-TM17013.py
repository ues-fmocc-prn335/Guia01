#CARNET: TM17013

def piramide_asteriscos(x):
    filas,r=1
    xsobrante=x-1 #los bloques sobrantes es igual a totalbloques-1
    if x > 2:
        while (xsobrante > r):
            filas=filas+1
            r=r+1 #r se comporta como la base
            xsobrante=xsobrante-r
        #niveles y bloques sobrantes
        print("El numero de niveles es", filas)
        print("Son ", xsobrante, " bloques sobrantes")
        for n in range(r+1): #mostrar piramide
            espacios=r-n
            print(' '*espacios+"* "*n)
    elif x <= 2: #validacion si ingresa 2 o menos
        print("No es piramide si tiene 2 bloques o menos")
        print("Ingrese un numero entero mayor a 2")

def decimal_binario(decimal):
    binario=''
    while decimal // 2 != 0:
        binario=str(decimal%2)+binario
        decimal=decimal // 2
    return str(decimal)+binario #retorna binario

def mostrar_menu():#menu
   print('\n1-Piramide con n bloques')
   print('2-Conversor de decimal a binario')
   print('3-Salir')


def main():
    while True:
        while True: #carga el menu
            try: # un try_except para los mensajes de error
                mostrar_menu()
                op = int(input("Digite la opcion:"))
                if  1 <= op <= 3: #validacion del menu
                    if op == 3:
                        print("Haz salido")
                        quit()
                    if op == 1:
                        asterisco = int(input("Ingrese el numero de bloques:"))
                        piramide_asteriscos(asterisco)
                    if op == 2:
                        numero = int(input('Introduce el número a convertir a binario: '))
                        print(decimal_binario(numero)) #imprime el resultado en binario
                else:
                    print("\nMensaje: Esa opcion no existe")
                    print()
            except ValueError:
              print("\nError en dato ingresado")
main()