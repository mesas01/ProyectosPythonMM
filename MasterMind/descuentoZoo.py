
edad = int(input("Digame su edad: "))
tipoDeCarnet = input("Digame su tipo de carnet (E para Estudiante / P Pensionista / F Familia numerosa / N Nada): ")

if (25 <= edad <= 35 and tipoDeCarnet == "E") or edad <= 10 or (edad >= 65 and tipoDeCarnet == "p") or (tipoDeCarnet == "f"):
    print("se te aplica eI descuento.")

else:
    print("no se te aplica eI descuento")
