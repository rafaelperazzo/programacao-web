# -*- coding: utf-8 -*-
# COLOQUE SUA BIBLIOTECA A PARTIR DAQUI

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
    
    

        

        
