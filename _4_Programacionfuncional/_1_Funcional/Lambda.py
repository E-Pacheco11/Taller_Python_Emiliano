if __name__ == '__main__':
    lambdasuma = lambda x,y: x + y
    valor1 = int(input("Dame un número:"))
    valor2 = int(input("Dame otro número:"))

    suma = lambdasuma(valor1,valor2)
    print(f"La suma de: {valor1} + {valor2} es = {suma}")
