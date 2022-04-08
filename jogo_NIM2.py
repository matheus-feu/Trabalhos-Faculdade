def main():
    opcao = 0
    while opcao != 1 and opcao != 2:
        print('Bem vindo ao jogo do NIM!\n')
        print('1 - Para iniciar a partida:')
        print('2 - Para não iniciar a partida:')
        opcao = int(input('Escolha sua opção:'))
    if opcao == 1:
        print('Você escolheu iniciar a partida!')
        partida()
    if opcao == 2:
        print('Você escolheu não iniciar a partida.')
        main()


def usuario_escolhe_jogada(n, m):
    usuario = True
    peças_jogada = int(input('Quantas peças você vai tirar?'))
    while peças_jogada > m or peças_jogada > n or peças_jogada <= 0:
        print('Oops! Jogada inválida! Tenta novamente.')
        peças_jogada = int(input('Quantas peças você vai tirar?'))
    return peças_jogada


def computador_escolhe_jogada(n, m):
    computador = True
    i = 1
    while i <= m and i <= n:
        if (n - 1) % (m + 1) == 0:
            return i
        else:
            i = i + 1
    if m <= n:
        return m


def partida():
    computador = False
    usuario = False

    n = int(input('Quantas peças?'))
    m = int(input('Limite de peças por jogada?'))

    if n % (m + 1) == 0:
        print('Você começa!')

        usuario = True
        peças_jogada = usuario_escolhe_jogada(n, m)
        n = n - peças_jogada
        print('Você tirou {} peças'.format(peças_jogada))
        if n != 0:
            print('Agora restam apenas {} peças no tabuleiro'.format(peças_jogada))
        if n == 0:
            print('Fim do jogo! Você ganhou!')
            global vj
            vj = vj + 1

        else:
            print('O computador começa!')
            computador = True
            peças_comp = computador_escolhe_jogada(n, m)
            n = n - peças_comp
            if peças_comp == 1:
                print('O computador tirou uma peça.')
            else:
                print('O computador tirou {} peças'.format(peças_comp))
            if n == 1:
                print('Agora restam apenas uma peça no tabuleiro.')
            elif n == 0:
                print('Fim do jogo! O computador ganhou!')

                global vc
                vc = vc + 1
            else:
                print('Agora restam apenas {} peças no tabuleiro'.format(n))

        while n > 0:
            # alternar as jogadas
            if computador == True:
                computador = False
                usuario = True
                peças_jogada = usuario_escolhe_jogada(n, m)
                n = n - peças_jogada
                if peças_jogada == 1:
                    print('Você tirou uma peça')
                else:
                    print('Você tirou {] peças'.format(peças_jogada))
                if n == 1:
                    print('Agora resta apenas uma peça no tabukeiro')
                elif n == 0:
                    print('Fim do jogo! Você ganhou!')
                vj = vj + 1
                break
            else:
                print('Agora restam {} peças no tabuleiro'.format(n))

            if usuario == True:
                usuario = False
                computador = True
                peças_comp = computador_escolhe_jogada(n, m)
                n = n - peças_comp
            if peças_comp == 1:
                print('O computador tirou uma peça.')
            else:
                print('O computador tirou {} peças.'.format(peças_comp))
            if n == 1:
                print('Agora resta apenas uma peça no tabuleiro.')
            elif n == 0:
                print('Fim do jogo! O computador ganhou!')
                vc = vc + 1
                break
            else:
                print('Agora restam apenas {} peças no tabuleiro'.format(n))

    vj = 0
    vc = 0

    main()