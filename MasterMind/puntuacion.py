

textoUsuario = input("Inrroduzca un texto: ")
espacios = 0
puntos = 0
comas = 0

for letra in textoUsuario:
    if letra == " ":
        espacios += 1
    elif letra == ".":
        puntos += 1
    elif letra == ",":
        comas += 1

print("Espacios: {}, puntos {}, comas {}".format(espacios, puntos, comas))
