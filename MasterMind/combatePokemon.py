import os
from random import randint

VIDA_INICIAL_PIKACHU = 80
VIDA_INICIAL_SQUIRTLE = 90

vida_pikachu = VIDA_INICIAL_PIKACHU
vida_squirtle = VIDA_INICIAL_SQUIRTLE

while vida_pikachu > 0 and vida_squirtle > 0:
    # Se desenvuelven los turnos de combate

    # Turno de Pikachu
    print("Turno de Pikachu")
    ataque_pikachu = randint(1, 2)
    if ataque_pikachu == 1:
        # Bola voltio
        print("Pikachu ataca con Bola Voltio")
        vida_squirtle -= 10
    else:
        print("Pikachu ataca con Onda Trueno")
        vida_squirtle -= 11

    if vida_squirtle < 0:
        vida_squirtle = 0

    if vida_pikachu < 0:
        vida_pikachu = 0

    barras_de_vida_pikachu = int(vida_pikachu * 10 / VIDA_INICIAL_PIKACHU)
    print("pikachu:     [{}{}] ({}/{})".format("*" * barras_de_vida_pikachu, " " * (10 - barras_de_vida_pikachu),
                                               vida_pikachu, VIDA_INICIAL_PIKACHU))

    barras_de_vida_squirtle = int(vida_squirtle * 10 / VIDA_INICIAL_SQUIRTLE)
    print("squirtle:    [{}{}] ({}/{})".format("*" * barras_de_vida_squirtle, " " * (10 - barras_de_vida_squirtle),
                                               vida_squirtle, VIDA_INICIAL_SQUIRTLE))

    input("Enter para continuar...\n\n")
    os.system("cls")

    # Turno de squirtle
    print("turno squirtle")

    ataque_squirtle = None
    while ataque_squirtle not in ["P", "A", "B", "N"]: #lista
        ataque_squirtle = input("¿Que égsas realizar? [P]lacaje, Pistola [A]gua, [B]urbuja, [N]ada: ")

    if ataque_squirtle == "P":
        print("squirtle ataca con placaje")
        vida_pikachu -= 10

    elif ataque_squirtle == "A":
        print("squirtle ataca con Pistola de agua")
        vida_pikachu -= 12

    elif ataque_squirtle == "B":
        print("squirtle ataca con Pistola de agua")
        vida_pikachu -= 9

    if vida_squirtle < 0:
        vida_squirtle = 0

    if vida_pikachu < 0:
        vida_pikachu = 0

    barras_de_vida_pikachu = int(vida_pikachu * 10 / VIDA_INICIAL_PIKACHU)
    print("pikachu:     [{}{}] ({}/{})".format("*" * barras_de_vida_pikachu, " " * (10 - barras_de_vida_pikachu),
                                               vida_pikachu, VIDA_INICIAL_PIKACHU))

    barras_de_vida_squirtle = int(vida_squirtle * 10 / VIDA_INICIAL_SQUIRTLE)
    print("squirtle:    [{}{}] ({}/{})".format("*" * barras_de_vida_squirtle, " " * (10 - barras_de_vida_squirtle),
                                               vida_squirtle, VIDA_INICIAL_SQUIRTLE))

    input("Enter para continuar...\n\n")
    os.system("cls")

    if vida_pikachu > vida_squirtle:
        print("picachu gana")
    else:
        print("squirtle gana")
