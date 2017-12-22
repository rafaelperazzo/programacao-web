# -*- coding: utf-8 -*-
# COLOQUE SUA BIBLIOTECA A PARTIR DAQUI
import random
def desenhaTabela(board):
    # Desenha a tabela

    # "board" é uma lista de 10 strings representando uma tabela (ignorando o indice [0])
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')

def solicitaSimboloDoHumano():
    # Escolhe a letra

    letter = ''
    while not (letter == 'X' or letter == 'O'):
        print('Você quer ser X ou O?')
        letter = input().upper()

    # Define a letra do computador
    if letter == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']
        
def sorteioPrimeiraJogada():
    # Escolhe quem joga primeiro
    if random.randint(0,1)== 0:
        return 'computer'
    else:
        return 'jogador'

def jogarNovamente():
    print('Quer jogar de novo? (s ou n)')
    return input().lower().startswith('s')

def fazerMovimento(board, letter, move):
    board[move] = letter

def verificaVencedor(bo, le):
    return ((bo[7] == le and bo[8] == le and bo[9] == le) or # topo
    (bo[4] == le and bo[5] == le and bo[6] == le) or # meio
    (bo[1] == le and bo[2] == le and bo[3] == le) or # baixo
    (bo[7] == le and bo[4] == le and bo[1] == le) or # vertical esquerdo
    (bo[8] == le and bo[5] == le and bo[2] == le) or # vertical meio
    (bo[9] == le and bo[6] == le and bo[3] == le) or # vertical direito
    (bo[7] == le and bo[5] == le and bo[3] == le) or # diagonal
    (bo[9] == le and bo[5] == le and bo[1] == le)) # diagonal

def mostrarTabuleiro(board):
    # Replicar a tabela com resultados
    dupeBoard = []

    for i in board:
        dupeBoard.append(i)

    return dupeBoard

def validaJogada(board, move):
    # Retorna true se o movimento feito é válido
    return board[move] == ' '


def movimentoRandomicoComputador(board, movesList):
    # Retorna um movimento válido randomico
    # Retorna "none" se não houver movimento válido
    possibleMoves = []
    for i in movesList:
        if validaJogada(board, i):
            possibleMoves.append(i)

    if len(possibleMoves) != 0:
        return random.choice(possibleMoves)
    else:
        return None

def jogadaComputador(board, computerLetter):
    # Retorna movimento do computer
    if computerLetter == 'X':
        playerLetter = 'O'
    else:
        playerLetter = 'X'

    ### IA ###
    # Checa se pode ganhar no proximo movimento
    for i in range(1, 10):
        copy = mostrarTabuleiro(board)
        if validaJogada(copy, i):
            fazerMovimento(copy, computerLetter, i)
            if verificaVencedor(copy, computerLetter):
                return i

    # Checa se o player pode ganhar no próximo movimento e bloqueia ele
    for i in range(1, 10):
        copy = mostrarTabuleiro(board)
        if validaJogada(copy, i):
            fazerMovimento(copy, playerLetter, i)
            if verificaVencedor(copy, playerLetter):
                return i

    # Tenta em uma das extremidades
    move = movimentoRandomicoComputador(board, [1, 3, 7, 9])
    if move != None:
        return move

    # Tenta no centro
    if validaJogada(board, 5):
        return 5

    # Tenta em um dos lados
    return movimentoRandomicoComputador(board, [2, 4, 6, 8])

def tabelaCompleta(board):
    # Retorna true se todos os espaços tiverem sido preenchidos
    for i in range(1, 10):
        if validaJogada(board, i):
            return False
    return True
        

        
