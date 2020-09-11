# Convertir decimal a binario
def toBinario(numero):
    resultado = ""
    while numero > 0:
        if numero % 2 == 1:
            resultado = resultado + "1"
        else:
            resultado = resultado + "0"
        numero = numero//2
    print("equivalente binario: {}".format(resultado[::-1]))
    
    
#imprimir piramide
def imprimirPiramide(bloques):
    niveles = []
    i = 1
    while i <= bloques:
        niveles.append(i)
        bloques = bloques - i
        i += 1
    i = 0
    for nivel in reversed(niveles):
        cadena = " " * i
        cadena = cadena + ("* " * nivel)
        i += 1
        niveles[nivel-1] = cadena

    for nivel in niveles:
        print(nivel)
    print("Bloques restantes: {}".format(bloques))


toBinario(int(input("\nIngrese el numero a convertir a binario ")))
imprimirPiramide(int(input("Ingrese la cantidad de bloques de la piramide ")))
