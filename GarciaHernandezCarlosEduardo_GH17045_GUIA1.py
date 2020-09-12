#Universidad de el Salvador - GUI1
#GarciaHernandez_CarlosEduardo GH17045

#Determinar la mediana de tres numeros

n1= int(input("Ingrese el primer numero"))
n2= int(input("Ingrese el segundo numero"))
n3= int(input("Ingrese el tercer numero"))

#creando funcion
def calcular_mediana(a, b, c):
    if (a>b):
        if(a<c):
            return a
        elif (b>c):
            return b
        else:
            return c
    else:
        if (a>c):
            return a
        elif (b<c):
            return b
        else:
            return c

print("\nla mediana ingresada es: ",calcular_mediana(n1, n2, n3))


#Determinando si el numero es un primo 

n = int(input("Ingrese un numero: "))

def evaluar_primo(n):
    contador =0
    resultado =True

    for i in range(1, n+1):
        if(n%i==0):
            contador+=1
        if(contador>2):
            resultado=False
            break
    return resultado

if (evaluar_primo(n)==True):
    print("el numero es primo")
else:
    print("el numero no es primo")