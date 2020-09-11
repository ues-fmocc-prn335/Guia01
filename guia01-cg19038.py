#Campos Guzmán, Juan Fracisco-CG19038
import os
def piramide():
    numBloque=input("Ingrese el numero de bloques: ")
    numBloque = int(numBloque)
    niveles=0
    numRecorrido=0
    numAcumulado=0
    contando=0
    estado=True
    while estado:
        numRecorrido= numRecorrido+1
        numAcumulado+=numRecorrido
        if numBloque<numAcumulado:
            estado=False
        else:
            niveles+=1
            contando+=numRecorrido
    cadena = "Sobran: "+str(numBloque-contando)+" bloques"
    print(cadena)
    cadena = "La piramide tiene: "+str(niveles)+" niveles"
    print(cadena)
    acumulador=1
    for nivel in range(0, niveles):
        if nivel==0:
            print(" "*(niveles), end="")
            print("*")
        else:
            print(" "*(niveles-acumulador), end="")
            print("* "*(acumulador+1))
            acumulador+=1
def conversor():
    numDecimal = input("Ingrese el numero en decimal a convertir: ")
    numDecimal = int(numDecimal)
    estado=True
    cadena=[]
    contador=0
    if numDecimal<0:
        estado=False
        print("Numero negativo")
    while estado:
        if numDecimal==1:
            cadena.insert((contador+1),"1")
            cadena = list(reversed(cadena))
            cadena = "".join(cadena)
            print("El numero en binario es: ", end="")
            print(cadena)
            estado = False
        else:
            residuo = numDecimal%2
            numDecimal = int(numDecimal/2)
            cadena.insert(contador,str(residuo))
            contador+=1

eleccion = 0
while eleccion >= 0 and eleccion<3:
    eleccion = input("\n¿Qué desea hacer?\n1-Graficar una pirámide\n"
           "2-Convertir de decimal a binario\n"
            "Cualquier otro número para salir\n")
    eleccion = int(eleccion)
    if eleccion==1:
        os.system("clear")
        piramide()
    elif eleccion==2:
        os.system("clear")
        conversor()
    else:
        quit()
