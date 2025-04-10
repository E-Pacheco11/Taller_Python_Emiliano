class ListaDatos:
   def __init__(self,matricula:str,estudiante:str, asignatura:str):
       self.matricula=matricula
       self.estudiante=estudiante
       self.asignatura=asignatura

if __name__ == '__main__':
    lista=[]
    lista.append(ListaDatos("12345678","Emiliano", "Programacion"))
    lista.append(ListaDatos("12569678","Gabriel", "Musica"))
    lista.append(ListaDatos("13465678","Abraham", "Idiomas"))
    lista.append(ListaDatos("12346598","Ricardo", "Artes escenicas"))
    for obj in lista:
        print(f"Nombre:{obj.estudiante}")
        print(f"Matricula:{obj.matricula}")
        print(f"Asignatura:{obj.asignatura}")
        print("-------------------------")