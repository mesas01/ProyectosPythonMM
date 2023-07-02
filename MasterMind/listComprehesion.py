
numerosIntroducidos = input("introduzca los números separadospor coma : ")  # 1,2,3,4,5
numerosDeUsusario = numerosIntroducidos.split(",")

numerosDeUsusario = [int(numero) for numero in numerosDeUsusario]  # filtra la lista y saca lo que sea int
# y lo pone en numero

print(numerosDeUsusario)

numeroPequenio = numerosDeUsusario[0]
numeroGrande = numerosDeUsusario[0]

for numero in numerosDeUsusario[1:]: # significa que arranca desde la casilla 1 hasta ek final
    if numeroPequenio > numero:
        numeroPequenio = numero

    if numeroGrande < numero:
        numeroGrande = numero

print("numero grande: {}, numero pequenio {}".format(numeroGrande, numeroPequenio))
