bloques= int(input("introduzca el numero de bloques que desea: "))
lineas=0
while bloques>lineas:
    lineas=lineas+1
    bloques=bloques-lineas
print("lineas de la piramides: ",lineas)
for i in range(lineas+1):
    espacios=lineas-1
    print(' '*espacios+' * '*i)
print("bloques sobrantes:", bloques)