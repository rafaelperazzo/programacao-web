# -*- coding: utf-8 -*-
# Minha bib
tabuleiro=[['','',''],['','',''],['','','']]


def solicitaSimboloDoHumano ():
    simboloJogador = input('Qual simbolo deseja ultilizar no jogo? ')
    while (simboloJogador != 'O')  and  (simboloJogador != 'X'):
        simboloJogador = input('Qual simbolo deseja ultilizar no jogo? ')
    return simboloJogador

def mostraTabuleiro(tabuleiro):
    print(matriz[0][0] + ' | ' + matriz[0][1] + ' | ' + matriz[0][2])
    print(matriz[1][0] + ' | ' + matriz[1][1] + ' | ' + matriz[1][2])
    print(matriz[2][0] + ' | ' + matriz[2][1] + ' | ' + matriz[2][2])
        