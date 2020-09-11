resultado=""
primocontador=0
try:
    numero=int(input("ingrese un numero para calcular si es primo o no\n"))
    if numero<0:
        print("error de dato ingresado, debeser positivo")
    else:
        for iteracion in range(1,numero+1):
            if(numero%iteracion)==0:
                primocontador=primocontador+1
        
        if primocontador==2:
                print("el numero es primo")
        else:
            print("el numero no es primo")    
except ValueError:
    print("error de rato ingresado, debe ser un numero positivo")
    