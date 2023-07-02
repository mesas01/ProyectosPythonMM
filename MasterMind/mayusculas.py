import string

textoDelUsuario = input("lntroduzca un texto: ")
letrasMayusculas = 0

for letra in textoDelUsuario:
    if letra in string.ascii_uppercase:
        letrasMayusculas += 1

print("Las mayusculas son: {}" .format(letrasMayusculas))
