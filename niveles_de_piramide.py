bloques=(input("ingrese el numero de piramides-->"))

try:
      bloques = int(bloques)
      a=True
except ValueError:
         a= False
if(a==False):
 print("ha ingresado una letra en vez de un dato entero")
elif (a==True):
 n=0
 total_debloques=bloques
 conter=1
 suma=0
 totaldebloques=0
 contador_de_bloques=0;
 todos=0
 numeroanterior=1;
 for i in range(bloques+1):
     if(i==numeroanterior):
         print("*"*conter)
         conter=conter+1
         contador_de_bloques=contador_de_bloques+conter-1
         numeroanterior=numeroanterior+conter
         numeroanterior=numeroanterior
        
 total_debloques=total_debloques-contador_de_bloques
 if(total_debloques==0):
     print("no ha sobrado ni un bloque")
     print(f"el total de bloques es: {contador_de_bloques}")
 else:
     print(f"han sobrado: {total_debloques} bloques")
     print(f"el total de bloques es: {contador_de_bloques}")