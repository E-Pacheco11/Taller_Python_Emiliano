class Datos:
    def __init__(self,nombre,correo,whatsapp): #Constructor
        self.nombre = nombre
        self.correo = correo
        self.whatsapp = whatsapp

    def setnombre(self, nombre:str):
        self.nombre =  nombre

if __name__ == '__main__':
    datos = Datos("Emiliano", "l222400442@smartin.tecn.mx", 2481851127)

    print(datos.nombre)
    datos.setnombre("Gaboopot")
    print(datos.nombre)
    datos.nombre="Emiliano"
    print(datos.nombre)
