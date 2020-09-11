try:
    print(format(int(input("Ingrese numero Decimal:")), "0b"))
except ValueError as e:
    print("ERROR: ",e)