
import random
if __name__ == '__main__':


    numero_aleatorio = random.randint(1, 10)


print("Adivina un número entre 1 y 10")
numero_usuario = int(input("¿Cuál es tu elección? "))


if numero_usuario == numero_aleatorio:
    print("¡¡Ganaste tu si le sabes!!")
else:
    print(f"¡Perdiste!, ponte chido {numero_aleatorio}")