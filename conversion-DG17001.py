def Convertir(decimal):
    # inicializo la variable

    binario = ''

    # calculo
    while decimal // 2 != 0:
        binario = str(decimal % 2) + binario
        decimal = decimal // 2

    # devuelvo el valor
    return str(decimal) + binario
