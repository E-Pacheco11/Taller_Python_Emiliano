def extraer(agenda: tuple ):
    i : int = 0
    while (i<len(agenda)):
        nombre, correo, tel = agenda[i]
        i+=1
        yield nombre,correo,tel

if __name__ == '__main__':

    agenda=[]
    agenda.append(("Juan", "juan@gmail.com", "222586985"))
    agenda.append(("Luis", "juan@gmail.com", "222586985"))
    agenda.append(("Miguel", "juan@gmail.com", "222586985"))
    agenda.append(("Jose", "juan@gmail.com", "222586985"))
    agenda.append(("Luis", "juan@gmail.com", "222586985"))
    agenda.append(("Armando", "juan@gmail.com", "222586985"))
    agenda.append(("Manzanero", "juan@gmail.com", "222586985"))
    agenda.append(("Julio", "juan@gmail.com", "222586985"))
    agenda.append(("Iglesias ", "juan@gmail.com", "222586985"))
    agenda.append(("Leonel", "juan@gmail.com", "222586985"))

    for a,b,c, in extraer(agenda):
        print(f"{a} , {b} , {c}")
