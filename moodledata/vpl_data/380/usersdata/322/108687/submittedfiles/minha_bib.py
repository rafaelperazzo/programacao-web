# -*- coding: utf-8 -*-
import random

tabuleiro = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
simbolos = ['X', 'O']
jogadasPossiveis = ['O','1','2']
def solicitaSimboloDoHumano():
    s = ''
    while True:
        s = input('\nQual símbolo você deseja utilizar no jogo? ')
        if not(s in simbolos):
            print('\nPor favor, selecione um símbolo válido: X ou O')
            continue

