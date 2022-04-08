# Autor(a)	    : Nome do(a) aluno (a):     Matheus Feu Soares de Assis  -  022291
# Data atual	: 26/03/2022
# Horário atual : 20:37 pm
# Trabalho 5

def main():
    opcao = 0
    while opcao != 1 and opcao != 2:
        linha = '-' * 50
        titulo = "Bem vindo ao jogo do NIM"
        print(linha)
        print(titulo.center(50))
        print(linha)

        print("1 - Para jogar uma partida.")
        print("2 - Para não jogar uma partida.")
        opcao = int(input("Escolha sua opção:"))
    if opcao == 1:
        print("\nVocê escolheu iniciar a partida!")
        partida()
    if opcao == 2:
        print("\nVocê escolheu não iniciar a partida!")
        main()


def partida():
    computador = False
    usuario = False

    n = int(input("\nQuantas peças? "))
    m = int(input("Limite de peças por jogada? "))

    if 0 == (n % (m + 1)):
        print("Você começa!")
        usuario = True
        pecas_jog = usuario_escolhe_jogada(n, m)
        n = n - pecas_jog
        print("Voce tirou {} peças.".format(pecas_jog))
        if n != 0:
            print("Agora restam {} peças no tabuleiro.".format(n))
        if n == 0:
            print("Fim do jogo! Você ganhou!")
            global vj
            vj = vj + 1

    else:
        print(" ")
        print("Computador começa!")
        computador = True
        pecas_comp = computador_escolhe_jogada(n, m)
        n = n - pecas_comp

        if pecas_comp == 1:
            print("\nO computador tirou uma peça.")
        else:
            print("O computador tirou {} peças!".format(pecas_comp))
        if (n == 1):
            print("Agora resta apenas uma peça no tabuleiro.")
        elif (n == 0):
            print("Fim do jogo! O computador ganhou!")
            global vc
            vc = vc + 1
        else:
            print("Agora restam {} peças no tabuleiro.".format(n))

    while n > 0:
        if computador:
            computador = False
            usuario = True
            pecas_jog = usuario_escolhe_jogada(n, m)
            n = n - pecas_jog
            if pecas_jog == 1:
                print("\nVocê tirou uma peça.")
            else:
                print("\nVocê tirou {} peças!".format(pecas_jog))
            if n == 1:
                print("Agora resta apenas uma peça no tabuleiro.")
            elif n == 0:
                print("Fim do jogo! Você ganhou!")

                vj = vj + 1
                break
            else:
                print("Agora restam {} peças no tabuleiro.".format(n))

        if usuario == True:
            usuario = False
            computador = True
            pecas_comp = computador_escolhe_jogada(n, m)
            n = n - pecas_comp

            if pecas_comp == 1:
                print("\nO computador tirou uma peça.")
            else:
                print("O computador tirou {} peças!".format(pecas_comp))
            if n == 1:
                print("Agora resta apenas uma peça no tabuleiro.")
            elif n == 0:
                print("Fim do jogo! O computador ganhou!")
                vc = vc + 1
                break
            else:
                print("Agora restam {} peças no tabuleiro.".format(n))


def computador_escolhe_jogada(n, m):
    computador = True
    i = 1
    while i <= m and i <= n:
        if (n - i) % (m + 1) == 0:
            return i
        else:
            i = i + 1
    if m <= n:
        return m


def usuario_escolhe_jogada(n, m):
    usuario = True

    pecas_jog = int(input("\nQuantas peças você vai tirar? "))
    while pecas_jog > m or pecas_jog > n or pecas_jog <= 0:
        print("\nOops! Jogada inválida! Tente novamente.")
        pecas_jog = int(input("\nQuantas peças você vai tirar? "))

    return pecas_jog


vj = 0
vc = 0

main()

