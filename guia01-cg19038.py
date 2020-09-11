#Campos Guzmán, Juan Fracisco-CG19038
import os
def piramide():
    estado=True
    while estado:
        numBloque=input("Ingrese el numero de bloques: ")
        try:
            numBloque = int(numBloque)
        except:
            print("Ingrese solo números")
            numBloque=-1
        if numBloque>=0:
            estado=False
        elif numBloque<1:
            print("Ingrese numeros positivos")
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
    estado=True
    while estado:
        numDecimal = input("Ingrese el número en decimal a convertir: ")
        try:
            numDecimal = int(numDecimal)
        except:
            print("Ingrese solo numeros")
            numDecimal=-1
        if numDecimal>=0:
            estado=False
        elif numDecimal<1:
            print("Ingrese numeros positivos")
    estado=True
    cadena=[]
    contador=0
    while estado:
        if numDecimal==1:
            cadena.insert((contador+1),"1")
            cadena = list(reversed(cadena))
            cadena = "".join(cadena)
            print("El número en binario es: ", end="")
            print(cadena)
            estado = False
        elif numDecimal==0:
            print("El número en binario es 0")
            estado=False
        else:
            residuo = numDecimal%2
            numDecimal = int(numDecimal/2)
            cadena.insert(contador,str(residuo))
            contador+=1

eleccion = 0
while eleccion >= 0 and eleccion<3:
    estado = True
    while estado:
        eleccion = input("\n¿Qué desea hacer?\n1-Graficar una pirámide\n"
           "2-Convertir de decimal a binario\n"
            "Cualquier otro número para salir\n")
        try:
            eleccion = int(eleccion)
        except:
            print("Ingrese solo números")
            eleccion=0
        if eleccion>0:
            estado=False
    if eleccion==1:
        os.system("clear")
        piramide()
    elif eleccion==2:
        os.system("clear")
        conversor()
    else:
        quit()
