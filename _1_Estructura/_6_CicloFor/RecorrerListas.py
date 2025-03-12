import sys

if __name__ == '__main__':
    lis=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
    #Una lista puede contener valores de diferente tipo
    #ademas una lista inmutable

    #for elemento in lista
    #print elemento

    lis.append(200)
    lis.append("Viernes")
    lis.append(False)
    lis.append(2.69)

    lis2=[1200,1300,1400]

    lis.append(lis2)

    for elemento in lis:
        print(elemento)

    nombre:str
    nombre="luis"
    nombre.join("Gutierrez")
    print(nombre)

    lis3=["Federico","Pablo", "Karla"]
    cadena:str=" - " .join(lis3)
    print(cadena)

    separado=cadena.split()
    for dato in separado:
