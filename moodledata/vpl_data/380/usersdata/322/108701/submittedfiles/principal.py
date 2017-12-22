# -*- coding: utf-8 -*-
from import jogoDaVelha_BIB

print ('Bem vindo ao jogo da velha do grupo')
nome = input('\nQual seu nome (ou apelido)? ')
simboloIndex = solicitaSimboloDoHumano()
primeiro = sorteioPrimeiraJogada(nome)
vezDoHumano = primeiro == 1
continuar = True
vencedor = 0

while continuar:
    if vezDoHumano:
        jogadaHumana(nome, simboloIndex)
        vencedor = verificaVencedor(nome, simboloIndex)
        
    if vencedor == 0:
        jogadaComputador(simboloIndex)
        mostraTabuleiro()
        vencedor=verificaVencedor(nome, simboloIndex)
        
    if vencedor == 999:
        mostraTabuleiro()
        print('Deu velha')
        break 
    
    elif vencedor == 3:
        mostraTabuleiro()
        print('Vencedor: %s' % nome)
        break
    elif vencedor == -3:
        mostraTabuleiro()
        print('Vencedor: %s' %' Computador')
        break
    vezDoHumano = True
    
        