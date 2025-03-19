import statistics as mate
if __name__ == '__main__':
    numeros = [10,20,50,80,90,30,40]

    conteo=0
    suma=0
    promedio=0
    for valor in numeros:
        suma+=valor
        conteo+=1

    promedio = suma/conteo
    print(promedio)

    #Opcion 2
    suma = 0
    print("opcion medio lenta")
    for valor in numeros:
        suma+=valor
        promedio = suma / len(numeros)
    print(promedio)

    #Opcion 3
    print("Opcion rapida")
    promedio == mate.mean(numeros)
    print(promedio)