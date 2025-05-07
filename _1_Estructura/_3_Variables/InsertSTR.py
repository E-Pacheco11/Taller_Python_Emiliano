if __name__ == '__main__':
    palabra : str = "%s"
    lista : list = ["Nombre", "A_pat", "Edad","Usuario","Correo_electronico", "Contrasennia"]

    print(palabra)
    #palabra= palabra * 5

    tamano = len(lista)#len obtiene la cantidad de elementos en una lista
    print(tamano)


    Campos = " ".join(lista)#Espacio vacio se considera objeto, contiene atributos y metodos
    print(Campos)

    palabra = palabra * len(lista)
    print(palabra)

    Campos = ",".join(lista)
    print(Campos)

    #querrySQL = querrySQL+palabra
    separacion = ",".join(palabra)

    querrySQL = f"INSERT INTO lista ({Campos}) VALUES  ({separacion}) "

    print(querrySQL)#Tarea separar "%s"