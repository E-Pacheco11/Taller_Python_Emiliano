import json

if __name__ == '__main__':
    #Version corta para abrir un archivo Json
    #Abre el archivo Json en modo de lectura y with se encarga de cerrarlo
    with open("datos.json", "r", encoding="utf-8") as archivo:
        datos = json.load(archivo)#Carga el contenido del archivo Json

    #Muestra el contenido del Json
    for persona in datos["personas"]:
        print("Nombre:", persona["nombre"])
        print("Edad:", persona["Edad"])
        print("Ciudad:", persona["Ciudad"])
        print("Estado", persona["Estado"])
        print("----------")#Linea en blanco para separacion
