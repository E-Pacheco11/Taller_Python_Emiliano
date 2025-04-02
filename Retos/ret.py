import json
import sys
BLACK = "\033[30m"
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
MAGENTA = "\033[35m"
CYAN = "\033[36m"
WHITE = "\033[37m"

def extrae():
    with open("EdadesBaseDeDatos.json", "r", encoding="utf-8") as archivo:
        EdadesBaseDeDatos = json.load(archivo)

    i = 1
    for elemento in EdadesBaseDeDatos["personas"]:
        yield(elemento["Id"],elemento["nombre"],elemento["Edad"], elemento["RFC"])
        match i:
            case 1:
                sys.stdout.write(RED)
            case 2:
                sys.stdout.write(BLUE)
            case 3:
                sys.stdout.write(GREEN)
            case 4:
                sys.stdout.write(YELLOW)
        i+=1





if __name__ == '__main__':
    #Version corta para abrir un archivo Json
    #Abre el archivo Json en modo de lectura y with se encarga de cerrarlo

    #Muestra el contenido del Json


    for Id, nombre,Edad, RFC in extrae():
        print(f"Id: {Id}")
        print(f"Nombre: {nombre}")
        print(f"Edad: {Edad}")
        print(f"RFC: {RFC}")


        if isinstance(Edad, int):
            if  Edad >= 18:
                print("Status: Mayor de edad")
            else:
                print("Status: Menor de edad")
        else:
            print("Status: Edad no válida o no especificada")

        print("----------")#Linea en blanco para separacion


