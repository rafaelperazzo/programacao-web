# -*- coding: utf-8 -*-
from jogoDaVelha_BIB import *

print('Bem vindo ao JogoDaVelha do grupo 8 [Iara, Ingrid, Luiz Otávio, Tatiane]\n')

#solicitar o nome da pessoa ou o apelido
nome = input('\nQual seu nome (ou apelido)? ')

#solicitar o símbolo da pessoa
simboloIndex = solicitaSimboloDoHumano()

#sortear a primeira jogada
primeiro = sorteioPrimeiraJogada(nome)

#primeiro == 0 é computador
def proximaJogada(primeiro):
    #mostar tela
    mostrar = False
    #joagada
    if primeiro == 0:
        jogadaComputador(simboloIndex)
        mostrar = True
    else:
        jogadaHumana(nome, simboloIndex)
    #mostrar a tela?
    if mostrar:
        mostraTabuleiro()
    #verificar vencedor
    if verificaVencedor(nome, simboloIndex):
        return
    proximaJogada(not primeiro)

proximaJogada(primeiro)