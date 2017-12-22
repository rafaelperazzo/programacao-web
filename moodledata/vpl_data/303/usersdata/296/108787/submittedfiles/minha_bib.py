# -*- coding: utf-8 -*-

#COMECE AQUI ABAIXO
import random

TURNO_JOGADOR = "jogador"
TURNO_COMPUTADOR = "computador"


def solicitar_simbolos():
    simbolo = str(input("Escolha um simbolo para jogar (X ou O): ")).lower()
    while simbolo != "x" and simbolo != "o":
        print("Simbolo invalido!")
        simbolo = str(input("Escolha um simbolo CORRETO para jogar! (X ou O): ")).lower()
    if simbolo == "x":
        return ['X', 'O']
    else:
        return ['O', 'X']


def sortear_primeiro_turno():
    if random.randint(1, 2) == 1:
        return TURNO_COMPUTADOR
    else:
        return TURNO_JOGADOR


def movimentacao_jogador(tabuleiro):
    """Função responsável por coletar informações da movimentação do jogador"""
    movimento = 0
    while 1 >= movimento <= 9 or not verificar_disponibilidade_posicao(tabuleiro, int(movimento)):
        posicao_selecionada = input("\nQual a sua jogada?")

        return {
            "0 0": 7,
            "0 1": 8,
            "0 2": 9,
            "1 0": 4,
            "1 1": 5,
            "1 2": 6,
            "2 0": 1,
            "2 1": 2,
            "2 2": 3
        }[posicao_selecionada]


def jogada(tabuleiro, simbolo, movimento):
    tabuleiro[movimento] = simbolo


def verificar_vencedor(tabuleiro, simbolo):
    return ((tabuleiro[1] == simbolo and tabuleiro[2] == simbolo and tabuleiro[3] == simbolo) or  # linhas vencedoras
            (tabuleiro[4] == simbolo and tabuleiro[5] == simbolo and tabuleiro[6] == simbolo) or
            (tabuleiro[7] == simbolo and tabuleiro[8] == simbolo and tabuleiro[9] == simbolo) or
            (tabuleiro[7] == simbolo and tabuleiro[4] == simbolo and tabuleiro[1] == simbolo) or  # colunas vencedoras
            (tabuleiro[8] == simbolo and tabuleiro[5] == simbolo and tabuleiro[2] == simbolo) or
            (tabuleiro[9] == simbolo and tabuleiro[6] == simbolo and tabuleiro[3] == simbolo) or
            (tabuleiro[7] == simbolo and tabuleiro[5] == simbolo and tabuleiro[3] == simbolo) or  # diagonais vencedoras
            (tabuleiro[9] == simbolo and tabuleiro[5] == simbolo and tabuleiro[1] == simbolo))


def tabuleiro_completo(tabuleiro):
    for i in range(1, 10):
        if verificar_disponibilidade_posicao(tabuleiro, i):
            return False
    return True


def verificar_disponibilidade_posicao(tabuleiro, movimento):
    """Verifica se a posição do tabuleiro está disponível"""
    return tabuleiro[movimento] == ' '


def efetuar_jogada_computador(tabuleiro, simbolo_computador):
    if simbolo_computador == "X":
        simboloJogador = "O"
    else:
        simboloJogador = "X"

    for i in range(1, 10):
        mostra = clonar_tabuleiro(tabuleiro)
        if verificar_disponibilidade_posicao(mostra, i):
            jogada(mostra, simbolo_computador, i)
            if verificar_vencedor(mostra, simbolo_computador):
                return i

    for i in range(1, 10):
        mostra = clonar_tabuleiro(tabuleiro)
        if verificar_disponibilidade_posicao(mostra, i):
            jogada(mostra, simboloJogador, i)
            if verificar_vencedor(mostra, simboloJogador):
                return i

    movimento = movimentar_aleatoriamente(tabuleiro, [1, 3, 7, 9])
    if movimento is not None:
        return movimento

    if verificar_disponibilidade_posicao(tabuleiro, 5):
        return 5

    return movimentar_aleatoriamente(tabuleiro, [2, 4, 6, 8])


def movimentar_aleatoriamente(tabuleiro, movimentos_efetuados):
    movimentos_possiveis = []
    for i in movimentos_efetuados:
        if verificar_disponibilidade_posicao(tabuleiro, i):
            movimentos_possiveis.append(i)

    if len(movimentos_possiveis) != 0:
        return random.choice(movimentos_possiveis)
    else:
        return None


def clonar_tabuleiro(tabuleiro):
    clone_tabuleiro = []

    for i in tabuleiro:
        clone_tabuleiro.append(i)

    return clone_tabuleiro


def desenhar_tabuleiro(tabuleiro):
    print(" " + tabuleiro[7] + " | " + tabuleiro[8] + " | " + tabuleiro[9])
    print("---+---+---")
    print(" " + tabuleiro[4] + " | " + tabuleiro[5] + " | " + tabuleiro[6])
    print("---+---+---")
    print(" " + tabuleiro[1] + " | " + tabuleiro[2] + " | " + tabuleiro[3])


def jogar_novamente():
    jogar = str(input("Você deseja jogar novamente? Digite 'sim' caso deseje.")).lower()
    return jogar == "sim"

