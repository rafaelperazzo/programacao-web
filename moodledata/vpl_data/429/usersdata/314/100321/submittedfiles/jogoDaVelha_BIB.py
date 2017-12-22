# -*- coding: utf-8 -*-
# Minha bib
def solicitaSimboloDoHumano ():
    simboloJogador = input('Qual simbolo deseja ultilizar no jogo? ')
    while (simboloJogador != 'O')  and  (simboloJogador != 'X'):
        simboloJogador = input('Qual simbolo deseja ultilizar no jogo? ')
    return simboloJogador