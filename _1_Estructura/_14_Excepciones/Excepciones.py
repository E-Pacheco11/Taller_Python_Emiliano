if __name__ == '__main__':
    try:
        #Codigo que puede causar una excepcion
        numero = int(input("Introduce un numero:"))
        resultado = 10 / numero

    except ValueError:
        #Manejo de la excepcion si se introduce un valor no valido
        print("¡Error! Debes introducir un numero entero.")
    except ZeroDivisionError:
        #Manejo de la excepcion si se intenta dividir por cero
        print("¡Error! No se puede dividir entre cero.")

    else:
        #Se ejecuta si no hubo excepciones
        print("El resultado es:" , resultado)

    finally:
        #Se ejecuta siempre, haya o no habido excepciones
        print("Fin del programa")