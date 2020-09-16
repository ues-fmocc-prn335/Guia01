def Calcular_mediana(a, b, c):
    if a >b:
        if a < c:
            return a
        elif b > c:
            return b
        else:
            return c
    else:
        if a > c:
            return c
        elif b < c:
            return b
        else:
            return c
print (Calcular_mediana(4, 5, 6))
lineas = int(input('Numero de lineas:'))
for numero_linea in range(lineas):
     espacios = lineas - numero_linea - 1
     asteriscos = 1 + numero_linea * 2
     print (" " * espacios + "*" * asteriscos)



