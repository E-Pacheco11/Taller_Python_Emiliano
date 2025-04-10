class Auto:
    marca="Honda" #Este es un atributo de la clase auto
    modelo=1000 #Esto es un atributo de la clase Auto
    placa="PCH-96-04" #Esto es un atributo de la clase auto

if __name__ == '__main__':
    taxi=Auto() #Esto es una instancia de la clase archivo
    miauto=Auto() #ESto es otra instancia de la misma clase

    print(taxi.placa) #Se invoca uno de los atributos de la clase auto
    miauto.placa="TCV-963-12"
    print(miauto.placa)