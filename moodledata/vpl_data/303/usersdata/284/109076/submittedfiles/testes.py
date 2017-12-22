from minha_bib import(solicitaSimboloDoHumano,sorteioPrimeiraJogada, jogadaHumana ,jogadaComputador,mostraTabuleiro,verificaVencedor,vazio,desenhaTabuleiro,jogarNovamente,movimentacao,movAleatoria,completo)

print('Bem vindo ao JogoDaVelha do grupo D')
nome = input('Qual o seu nome (ou apelido)? ')
while True:
    tabul = [' '] * 10
    letraJogador, letraComputador = solicitaSimboloDoHumano()
    turno = sorteioPrimeiraJogada()
    print('Vencedor do sorteio para início do jogo: {}'.format(turno))
    rodando = True

    while rodando:
        if turno == 'Jogador':
            desenhaTabuleiro(tabul)
            movimento = jogadaHumana(tabul,nome)
            movimentacao(tabul, letraJogador, movimento)

            if verificaVencedor(tabul, letraJogador):
                desenhaTabuleiro(tabul)
                print('Vencedor: {}'.format(nome))
                rodando = False
            else:
                if completo(tabul):
                    desenhaTabuleiro(tabul)
                    print('Deu Velha!')
                    break
                else:
                    turno = 'Computador'

        else:
            movimento = jogadaComputador(tabul, letraComputador)
            movimentacao(tabul, letraComputador, movimento)

            if verificaVencedor(tabul, letraComputador):
                desenhaTabuleiro(tabul)
                print('Vencedor: Computador')
                rodando = False
            else:
                if completo(tabul):
                    desenhaTabuleiro(tabul)
                    print('Deu Velha!')
                    break
                else:
                    turno = 'Jogador'

    if not jogarNovamente():
        break
