bloq = int(input("Ingrese el numero de bloques que desee: "))
base=1
levels=1
av=bloq-1

if bloq<=2:
    print("El numero debe ser mayor a 2")
else:
    while(av>base):
        levels=levels+1
        base=base+1
        av=av-base

    print("El numero de niveles es: ", levels)
    print("Sobran ",av," bloques")

    for i in range(base+1):
        print("**" * i)