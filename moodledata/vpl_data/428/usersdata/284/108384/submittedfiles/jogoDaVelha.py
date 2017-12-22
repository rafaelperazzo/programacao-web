# -*- coding: utf-8 -*-
from jogoDaVelha_BIB import(solicitaSimboloDoHumano,sorteioPrimeiraJogada, jogadaHumana ,jogadaComputador,mostraTabuleiro,verificaVencedor,vazio,desenhaTabuleiro,jogarNovamente,movimentacao,movAleatoria,completo)

# COLOQUE SEU PROGRAMA A PARTIR DAQUI


print('Bem vindo ao JogoDaVelha do grupo Thayná, Marlon e Fábio')
nome = input('Qual o seu nome (ou apelido)? ')
while True:
    tabul = [' '] * 10
    letraJogador, letraComputador = solicitaSimboloDoHumano()
    turn = sorteioPrimeiraJogada()
    print('Vencedor do sorteio para início do jogo: {}'.format(turn))
    rodando = True

    while rodando:
        if turn == 'Jogador':
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
                    turn = 'Computador'

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
                    turn = 'Jogador'

    if not jogarNovamente():
        break
