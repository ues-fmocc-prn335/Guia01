# importo la funcion
import math


def Primo(numero):
    # valido que sea positivo
    if (numero <= 1):
        return False

    # Calculo
    for i in range(2, math.ceil(math.sqrt(numero)) + 1):
        if (numero % i == 0 and i != numero):
            # devuelvo un valor
            return False
    return True
