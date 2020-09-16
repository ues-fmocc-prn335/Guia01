
# Nombre de usuario en GitHub:  Ivan9962

def esPrimo(num):
    if num < 1:
        return False
    elif num == 2:
        return True
    else:
        for i in range(2, num):
            if num % i == 0:
                return False
        return True


def app():
    num = int(input('Escribe un numero: '))
    result = esPrimo(num)

    if result is True:
        print('El numero ingresado es primo')
    else:
        print('EL numero ingresado NO es primo')


if __name__ == '__main__':
    app()






