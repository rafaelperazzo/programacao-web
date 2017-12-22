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
