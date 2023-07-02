listaDeLaCompra = []
inputDeUsuario = None

print("Programa de la compra de la lista\n")

while True:
    inputDeUsuario = input("¿que desea comprar? ([Q] para salir)")
    if inputDeUsuario == "Q":
        break  # pass = no hacer nada
    elif inputDeUsuario in listaDeLaCompra:
        print("{} ya esta en la lista".format(inputDeUsuario))
    else:
        if input("¿Seguro que quiere añadir {} a la lista de la compra? [S/N]".format(inputDeUsuario)) == "S":
            listaDeLaCompra.append(inputDeUsuario)  # append es añadir al final de la lista

print("la lista de la compra es: ")
print(listaDeLaCompra)
