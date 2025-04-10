class ListaDatos:
   def __init__(self,matricula:str,estudiante:str, asignatura:str):
       self.matricula=matricula
       self.estudiante=estudiante
       self.asignatura=asignatura

class ControlEscolar(ListaDatos):
    def __init__(self):
        self.lista=[]
    def addEstudiante(self,estudiante,matricula,asignatura):
        self.lista.append(ListaDatos(matricula,estudiante,asignatura))

    def show(self):
        for obj in self.lista:
            print(f"Nombre: {obj.estudiante}")
            print(f"Matricula: {obj.matricula}")
            print(f"Asignatura: {obj.asignatura}")



if __name__ == '__main__':
   escolar=ControlEscolar()
   escolar.addEstudiante("Emiliano","123456","Programacion")
   escolar.show()


