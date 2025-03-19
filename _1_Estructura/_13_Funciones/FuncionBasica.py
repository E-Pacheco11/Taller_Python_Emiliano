
def suma(a,b)->int:
    return a+b

def sumalista(lista:list)->int:
    return sum(lista)

if __name__ == '__main__':
    print(f"La suma es {suma (15, 22)}")

    lista=[1,2,3,4,5]

    print(f"La suma de la lista es: {sumalista(lista)}")
