numero_entero=(input("ingrese un numero-->"))
contador=0
primo=0
i=1
try:
      numero_entero = int(numero_entero)
      a=True
except ValueError:
         a= False

if(a==False):
 print ("el dato ingresado es incorrecta: escribe un numero entero")
elif (a==True):
 while i<=numero_entero+1:
   primo=numero_entero%i
   if(primo==0):
    contador+=1
      

   i+=1
 if(contador!=2):
    print("el numero ingresado no es primo")
 else:
    print("el numero ingresado es primo")