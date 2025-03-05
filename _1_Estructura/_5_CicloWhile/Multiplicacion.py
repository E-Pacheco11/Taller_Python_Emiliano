if __name__ == '__main__':
    x = int(input("Ingrese un valor para x:"))
    y = int(input("Ingrese un valor para y:"))

    i: int = 1
    multi: int = 0

    while i<=y:
        multi = multi+x
        i+=1
    print(f"El resultado de {x} * {y}={multi}")