# Autor(a)	    : Nome do(a) aluno (a):     Matheus Feu Soares de Assis  -  022291
# Data atual	: 16/03/2022
# Horário atual : 22:37 pm
# Trabalho 4

número = int(input('Digite um número:'))
tot = 0
for contador in range(1, número + 1):
    if número % contador == 0:
        print('\033[33m', end='')
        tot += 1
    else:
        print('\033[31m', end='')
    print('{} '.format(contador), end='')
print('\n\033[m0 número {} foi divisível {} vezes'.format(número, tot))
if tot == 2:
    print('Portanto, ele É PRIMO!')
else:
    print('Portanto, ele NÃO É PRIMO!')





