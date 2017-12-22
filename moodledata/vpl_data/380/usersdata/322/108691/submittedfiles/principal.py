# -*- coding: utf-8 -*-
from jodoDaVelha_BIB import *

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
        mostrartabuleiro()
        vencedor=verificaVencedor(nome, simboloIndex)
        
    if vencedor = 999:
        mostrar tabuleiro()
        print('Deu velha')
        break 
    
    elif vencedor == 3:
        mostrar tabuleiro()
        print('Vencedor: %s' %' nome)
        break
    elif vencedor == -3:
        mostrar tabuleiro()
        print('Vencedor: %s' %' Computador)
        break
    vezDoHumano = True
    
        