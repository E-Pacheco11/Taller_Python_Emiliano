if __name__ == '__main__':
    nombre1 = str (input("Proporciona el primer nombre:"))
    nombre2 = str (input("Proporciona el segundo nombre:"))

    n1 = len(nombre1)
    n2 = len(nombre2)

    if n1>n2:
        print(f"El nombre mas largo es {nombre1} con {n1} letras")

    else:
        if len(nombre1) == len(nombre2):
            print("Los nombres son iguales")
        else:
            print(f"El nombre mas largo es {nombre2} con {n2} letras")



