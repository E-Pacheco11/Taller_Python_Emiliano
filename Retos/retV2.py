import json
import sys
RESET = "\033[0m" # Restablece el color a su valor por defecto
BLACK = "\033[30m"
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
MAGENTA = "\033[35m"
CYAN = "\033[36m"
WHITE = "\033[37m"

def extrae():
    try:
        archivo = open("123.json", "r", encoding="utf-8")
        #Carga el contenido del archivo
        EdadesBaseDeDatos = json.load(archivo)

        #Recorre la lista de personas e imprime cada una

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
                case 5:
                    sys.stdout.write(MAGENTA)
            i+=1
    except FileNotFoundError:
        print(RED,"¡Eror! El archivo no exite")
    except json.JSONDecodeError:
        print(RED, "¡Error! El archivo no contiene un Json válido")
    except Exception as e:
        print(GREEN, "No se que ocurrió", e)
    else:
        #Cierra el archivo manualmente
        archivo.close()
        print(RESET, "Archivo json cerrado")





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


