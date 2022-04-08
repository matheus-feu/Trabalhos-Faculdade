def fatorial():
    n = int(input('Digite um número inteiro:\n'))

    fator = 2
    while n != 1:
        mult = 0
        while n % fator == 0:
            n = n / fator
            mult = mult + 1
        if mult != 0:
            print('O fator do número é {} e sua multiplicidade é {}.'.format(fator, mult))
        fator = fator + 1


fatorial()
