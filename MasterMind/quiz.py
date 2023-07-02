
titulo = "Bienvenido al Test sobre el queso"
print("\n" + titulo + "\n" + "-" * len(titulo) + "\n")

puntuacion = 0

opcion = input("Pregunta 1: Que haces cuando ves una tabla de quesos?\n"
               "A. salgo corriendo\n"
               "B. Pruebo uno de los quesos o incluso varios\n"
               "C. No evitar devorarla\n")

if opcion == "A":
    puntuacion += 0
elif opcion == "B":
    puntuacion += 5
elif opcion == "C":
    puntuacion += 10
else:
    print("Las opciones posibles son A, B y C")
    exit()

opcion = input("pregunta 2: ¿como te gusta la hamburguesa\n"
               "A. sin queso\n"
               "B. com queso\n"
               "C. pan y queso\n")

if opcion == "A":
    puntuacion += 0
elif opcion == "B":
    puntuacion += 5
elif opcion == "C":
    puntuacion += 10
else:
    print("Las opciones posibles son A, B y C")
    exit()

opcion = input("pregunta 3: ¿Eres intolerante a la lactosa ? \n"
               "A. si\n"
               "B. a veces\n"
               "C. no\n")

if opcion == "A":
    puntuacion += 0
elif opcion == "B":
    puntuacion += 5
elif opcion == "C":
    puntuacion += 10
else:
    print("Las opciones posibles son A, B y C")
    exit()

if puntuacion >= 25:
    print("ResuItado: Felicidades, eres fanático de los quesos")

elif puntuacion >= 15:
    print("Resultado: Felicidades, eres una persona que Ie gusta eI queso")

else:
    print("Resultado: felicidades no te gusta eI gueso")
