import random

linha = 50 * '-'
title = 'Bem vindo ao Gerador de Senhas!'
print(linha)
print(title.center(50))
print(linha)

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%&*().,?0123456789'

number = input('\nQuantidade de caracteres para criar a senha:')
number = int(number)

length = input('Comprimento da sua senha:')
length = int(length)

print('\nAqui está sua senha:')

for pwd in range(number):
    passwords = ''
    for c in range(length):
        passwords += random.choice(chars)
    print(passwords)

