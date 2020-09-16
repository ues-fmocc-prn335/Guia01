bloques= int(input("Introduzca cuantos bloques desea colocar: "))
lineas=0
while bloques>lineas:
    lineas=lineas+1
    bloques=bloques-lineas
print("Lineas de la piramide: ",lineas)
for i in range(lineas+1):
    espacios=lineas-i
    print(' '*espacios+' * '*i)
print("Los bloques sobrantes: ",bloques)
