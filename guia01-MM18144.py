
#funcion para determinar si un numero es primo
def numeroPrimo():
    numero=int(input("proporcione un numero"))
    contador=0 #contador que posteriormente servira para saber cuantas veces da el residuo decero
    
    for i in range(1, numero+1):
        if(numero%i==0): #un numero es primo cuando solo es divisible entre 1 y el mismo
            contador=contador+1
    else:
        if(contador==2): 
            print(numero, "Si es un numero primo")
        else:
            print(numero, "No es un numero primo") 
            
            
#funcion para determinar la mediana de 3 numeros            
def medianaTresNumeros():
    lista=[]  #declaramos una lista vacia
    i=0
    while(i<3):
        num=int(input("ingrese un numero"))
        lista.append(num) # el append servira para agregar los valores ingresados a la lista
        i=i+1
    print("numeros ingresados: ",lista)
    lista.sort()  #.sort servira para ordenar los datos
    print("numeros ordenados: ", lista)
    print("la mediana es: ",lista[1])
                           

def menu():
    
    while True:
        eleccion=int(input("que accion realizara?\n"+
                           "1- Determinar si un numero es primo\n"+
                           "2- Determinar la mediana de 3 numeros\n"+
                           "3- Salir"))
        if(eleccion==1):
            numeroPrimo()
        if(eleccion==2):
            medianaTresNumeros()
        if(eleccion==3):
            print("-----------------")  
            break                  
menu()    
    