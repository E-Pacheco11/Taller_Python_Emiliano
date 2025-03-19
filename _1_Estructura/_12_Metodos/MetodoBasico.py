import statistics as mate

#def suma(a:int, b:int):
 #   print(f"La suma de: {a} + {b} es: {a+b}")

def suma(a:int, b:int , c=None):
    if c is None:
        print(f"La suma de {a} + {b} es: {a+b} ")
    else:
        print(f"La suma de {a} + {b} + {c}  es: {a+b+c}")

        if b and c is None:
            print(f"El unico elemento es: {a} la suma de {a} + {a} es: {a+a}")
        else:
            print(f"la suma de {b} + {c} es: {b+c}")

def promedioArreglo(lista):
    lista.append(5)
    lista.append(45)
    lista.append(56)
    p=mate.mean(lista)
    print(f"El promedio es {p}")


if __name__ == '__main__':

    suma(10,52)
    suma(23,47 ,50)


    lista2= [1,2,3,4,5,6,7,8,9,10]
    promedioArreglo(lista2)
    print(lista2)

