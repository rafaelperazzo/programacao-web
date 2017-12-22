# -*- coding: utf-8 -*-
from minha_bibpy import *

print("Bem vindo ao Jogo da Velha do grupo")

#solicitar o nome da pessoa ou o apelido
nome = input('\nQual seu nome (ou apelido)? ')

#solicitar o símbolo da pessoa
simboloIndex = solicitaSimboloDoHumano()

#sortear a primeira jogada
primeiro = sorteioPrimeiraJogada(nome)

#primeiro == 0 é computador
#vezDoHumano
vezDoHumano = primeiro == 1
#primeiro == 0 é computador
continuar = True
vencedor = 0
while continuar:
    #
    if vezDoHumano:
        #jogada do humano
        jogadaHumana(nome, simboloIndex)
        vencedor = verificaVencedor(nome, simboloIndex)
    #
    if vencedor == 0:
        #jogada do computador
        jogadaComputador(simboloIndex)
        mostraTabuleiro()
        vencedor = verificaVencedor(nome, simboloIndex)
    #
    if vencedor == 999:
        mostraTabuleiro()
        print('Deu velha')
        break
    elif vencedor == 3:
        mostraTabuleiro()
        print('Vencedor: %s' % nome)
        break
    elif vencedor == -3:
        print('Vencedor: %s' % 'Computador')
        break
    #
    vezDoHumano = True