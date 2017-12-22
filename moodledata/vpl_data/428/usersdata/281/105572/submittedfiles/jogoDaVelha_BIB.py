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
        
def sorteioPrimeiraJogada():
    # Escolhe quem joga primeiro
    if random.randint (0,1) == 0:
        return 'computer'
    else:
        return nomeJogador
        
