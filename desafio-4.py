# Autor(a)	    : Nome do(a) aluno (a):     Matheus Feu Soares de Assis - 022291
# Data atual	: 16/03/2022
# Horário atual : 05:36 am

# Algoritmo para cálculo de média dos alunos.

# - Média abaixo de 5.0: REPROVADO!
# - Média entre 5.0 e 6.9: RECUPERAÇÃO!
# - Média 7.0 ou superior: APROVADO!

nota1 = float(input('Primeira nota do aluno:'))
nota2 = float(input('Segunda nota do aluno:'))
média = (nota1 + nota2) / 2

print('Tirando a nota entre {:.1f} e {:.1f} a média do aluno é: {:.1f}'.format(nota1, nota2, média))

if média >= 5 and média < 7:
    print('O Aluno está RECUPERAÇÃO!')
#   N1 = 6.5, N2 = 4.5
elif média < 5:
    print('O Aluno está REPROVADO!')
    #   N1 = 2, N2 = 4
elif média >= 7:
    print('O Aluno está APROVADO!')
    #   N1 = 9, N2 = 7


