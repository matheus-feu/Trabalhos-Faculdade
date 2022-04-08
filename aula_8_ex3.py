def mdc(x, y):
    while y != 0:
        resto = x % y
        x = y
        y = resto

    return x


def main():
    print("Esse programa faz o cálculo de Algoritmo de Euclides\n")
    x = int(input("Informe o valor de x: "))
    y = int(input("Informe o valor de y: "))

    print("\nO Máximo Divisor Comum de {} e {} é: {}".format(x, y, mdc(x, y)))


if __name__ == "__main__":

    main()