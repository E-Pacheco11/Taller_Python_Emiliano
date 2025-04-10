class Hospital:
    def __init__(self):
        self.__NombrePaciente:str=""
        self.__nss:int=1258
        self.__enfermedad:str=""

    def __getNombrePaciente(self)->str:
        return self.__NombrePaciente
    def getNss(self)->int:
        return self.nss
    @property #Metodo de propiedad para solo lectura
    def getEnfermedad(self)->str:
        return self.enfermedad

    def setNombrePaciente(self,nombre:str):
        self.__NombrePaciente=nombre
    def setNss(self,nss:int):
        self.nss=nss
     #Esto convierte el metodo en una propiedad de solo es escritura
    def setEnfermedad(self,enfermedad:str):
        self.enfermedad=enfermedad


if __name__ == '__main__':
    hospital=Hospital()
    hospital.__NombrePaciente="Juan"

    print(hospital.getNombrePaciente())
