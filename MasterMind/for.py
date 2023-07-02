
vocales = "aeiou"
frase = "hola estoy aprandiendo python"
vocalesEncontradas = 0

for letra in frase:
    if letra in vocales:
        print("He encontrado una '{}'".format(letra))
        vocalesEncontradas += 1

print("vocales encontradas: {}".format(vocalesEncontradas))
