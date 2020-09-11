# Nombre: Julio Eduardo Aguilar García
# CARNE: AG19045

import math
import os

def App():
    limpiar()
    while True:
        try:
            print("MENU")
            print("1) Determinar un numero primo")
            print("2) Determinar el nivel de una piramide")
            print("PRESIONE CUALQUIER OTRO NUMERO PARA SALIR")
            opcion = int(input("Ingrese una opcion: "))

            limpiar()

            if (opcion == 1):
                try:
                    print("DETERMINAR UN NUMERO PRIMO")
                    numero = int(input("Ingresa un numero: "))

                    determinar_primo(numero)
                except:
                    print("EL VALOR INGRESADO NO ES VALIDO \n")
                    continue
            elif (opcion == 2):
                try:
                    print("DETERMINAR EL NIVEL DE UNA PIRAMIDE")
                    bloques = int(input("Ingresa un numero de bloques: "))

                    determinar_nivel_priramide(bloques)
                except:
                    print("EL VALOR INGRESADO NO ES VALIDO \n")
                    continue
            else:
                break
            print("\r")
        except:
            limpiar()
            continue

def limpiar():
    os.system("cls")

def determinar_primo(numero):
    contador = 0
    divisor = 0

    if (numero > 0):
        while (divisor <= numero):
            divisor += 1
            if (numero % divisor == 0):
                contador += 1
        if (contador == 2):
            print(f"{numero} ES UN NUMERO PRIMO")
        else:
            print(f"{numero} NO ES UN NUMERO PRIMO")
    else:
        print("EL NUMERO INGRESADO NO ES VALIDO")

def determinar_nivel_priramide(bloques):
    if (bloques > 0):
        niveles = (math.sqrt(1 + 8*bloques)-1)/2

        if (niveles % int(niveles) == 0):
            print(f"EL NUMERO DE NIVELES DE UNA PIRAMIDE QUE SE PUEDE FORMAR CON {bloques} BLOQUES ES: {int(niveles)}")
        else:
            siguiente_nivel = int(niveles) + 1
            bloques_siguiente_nivel  = int((siguiente_nivel*(siguiente_nivel+1))/2)
            bloques_faltantes = bloques_siguiente_nivel - bloques

            print(f"FALTAN {bloques_faltantes} BLOQUES PARA PODER FORMAR UNA PIRAMIDE DE {siguiente_nivel} NIVELES")        
    else:
        print("EL NUMERO DE BLOQUES INGRESADO NO ES VALIDO")

App()
