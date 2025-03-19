if __name__ == '__main__':
    #añade un elemento al final de la lista
    print("Añade un elemento al final de la lista con .append")
    mi_lista= [1,2,3]
    mi_lista.append(4)
    print(mi_lista)

    #añade los elementos a otra lista
    print("Añade otra lista a la lista original con .extend")
    mi_lista=[1,2,3]
    otra_lista=[4,5,6]
    mi_lista.extend(otra_lista)
    print(mi_lista)

    #Insert añade un elemento en una posicion especifica en la lista
    print("Lista con .insert para un lugar en especifico")
    mi_lista = [1,2,3]
    mi_lista.insert(1,4)
    print(mi_lista)

    #Elimina el primer elemento encontrado en la lista
    print("Elimina el primer elelemnto econtrado en la lista con .remove")
    mi_lista=[1,2,3]
    mi_lista.remove(2)
    print(mi_lista)

    #Elimina y devuelve un elemento a la lista
    print("Elimina y devuelve un elemento a la lista con .pop ")
    mi_lista=[1,2,3]
    elemento = mi_lista.pop(1)
    print(f"elemento eliminado {elemento} ")
    print(mi_lista)

    #Devuelve el indice de la primera aparicion de
    print("Imprime el indice de la lista con .index ")
    mi_lista=[1,2,3]
    indice = mi_lista.index(2)
    print(f"El indice de la lista es: {indice} ")

    #Devuelve el numero de veces que aparece un elemento en la lista
    mi_lista=[1,2,3,2]
    conteo = mi_lista.count(2)
    print(f"El elemento que mas se repite es el: {conteo}")

    #Ordena los elementos de la lista de forma ascendente
    mi_lista=[3,1,4,2]
    mi_lista.sort()
    print(mi_lista)

    #Para ordenar de manera descendente
    mi_lista=[3,1,4,2]
    mi_lista.sort(reverse=True)
    print(f"La lista al reverso es: {mi_lista}")

    #Invierte el orden de los elementos de la lista
    mi_lista=[1,2,3,4]
    mi_lista.reverse()
    print(mi_lista)

    #Elimina todos los elementos de la lista
    mi_lista=[1,2,3]
    mi_lista.clear()
    print(f"Lista borrada:{mi_lista}")

    #Crea una copia superficial de la lista
    mi_lista=[1,2,3]
    copia_lista = mi_lista.copy()
    mi_lista.append(4)
    print(copia_lista)

    #