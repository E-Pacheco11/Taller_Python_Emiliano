class Libro:

    def __init__(self, ISBN:int, Titulo:str, Autor:str):
        self.__ISBN:int = ISBN
        self.__Titulo:str= Titulo
        self.__Autor:str= Autor
        self.lista=[]
    def __getISBN(self)->int:
        return self.__ISBN
    def __getTitulo(self)->str:
        return self.__Titulo
    def __getAutor(self)->str:
        return self.__Autor

class RegistroLibros:
    def addLibro(self,ISBN,Titulo,Autor):
        self.lista.append(Libro(ISBN,Titulo,Autor))

    def show(self):
        for obj in self.lista:
            print(f"El ISBN es: {obj.__ISBN}")
            print(f"El titulo es: {obj.__Titulo}")
            print(f"El autor es: {obj.__Autor}")


if __name__ == '__main__':
    Biblioteca = RegistroLibros()
    Libro.addLibro( 1234,"El principito","Antoine de Saint-Exupery")
    Libro.addLibro("Frankstein", 2431,"Antoine de Saint-Exupery")
    Libro.addLibro("El cascanueces", 1234,"Antoine de Saint-Exupery")
    Libro.addLibro("Dumbo", 1234,"Antoine de Saint-Exupery")
    Biblioteca.show()