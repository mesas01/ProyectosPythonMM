def fibonacci_recursivo(n):
    if n <= 1:
        return 1
    return fibonacci_recursivo(n - 1) + fibonacci_recursivo(n - 2)


def potencia(numero, base=2):
    resultado = numero
    for a in range(1, base):  # desde el numero al numero de la base
        resultado *= numero
    return resultado


def main():
    for a in range(10):
        print(fibonacci_recursivo(a))
        
    print(potencia(4))
    print(potencia(4, 5))


if __name__ == "__main__":
    main()
