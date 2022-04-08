# Autor(a)	    : Nome do(a) aluno (a):     Matheus Feu Soares de Assis - 022291
# Data atual	: 17/03/2022
# Horário atual : 14:44 pm
# Trabalho 4

número_salvo = n = int(input('Digite um número para verificar se contém números adjacentes iguais:'))

anterior = n % 10
n = n // 10;
adj_iguais = False;
pos = 0

while n > 0 and not adj_iguais:
    atual = n % 10
    if atual == anterior:
        adj_iguais = True
    else:
        pos += 1
    anterior = atual
    n = n // 10

if adj_iguais:
    print('Sim, {} possui números {} adjacentes.'.format(número_salvo,atual))
else:
    print('{}, não possui números adjacentes.'.format(número_salvo))