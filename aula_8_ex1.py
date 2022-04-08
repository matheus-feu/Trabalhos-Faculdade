n = int(input('Digite o índice da série de Fibonacci:\n'))


def Tribonacci(n):
    if n == 1 or n == 2:
        return 1
    elif n == 3:
        return 2
    else:
        return Tribonacci(n - 1) + Tribonacci(n - 2) + Tribonacci(n - 3)


print('O número de Tribonacci é {}:'.format(Tribonacci(n)))
