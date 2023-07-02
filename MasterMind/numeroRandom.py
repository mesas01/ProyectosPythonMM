import random

numeroGanador = random.randint(1, 10)
numeroElegido = int(input("Elige un numero: "))

if numeroElegido == numeroGanador:
    print("has ganaddo")

if numeroElegido > 10:
    print("Te has pasado un poco... Era entre 1 y 10.")

if numeroElegido < 1:
    print("te has quedado corto.")

if numeroElegido == 666:
    print("has elegido el número de la bestia.")

if numeroElegido == -666:
    print("Has el número de la bestia, pero además en negativo, eso es doblemente maligno")

print("E1 número ganador era: {} " .format(numeroGanador))
