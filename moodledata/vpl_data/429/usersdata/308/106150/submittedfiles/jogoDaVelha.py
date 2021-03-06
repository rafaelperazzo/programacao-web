# -*- coding: utf-8 -*-
from jogoDaVelha_BIB import *
from os import system
while True:
    visual = [[' ',' ', ' '], [' ', ' ',' '], [' ', ' ', ' ']]  
    nomes = [['', ''], ['Computador', '']]
    vencedor = ' '
    print('Bem Vindo ao Jogo da Velha do Grupo A: Deu Velha')
    nomes[0][0]=solicitaNomeDoJogador()
    a=solicitaSimboloDoHumano()
    nomes[0][1]=a[0]
    nomes[1][1]=a[1]

    i = sorteioPrimeiraJogada(nomes)
    a = i
    while i<9+a:
        if i%2 == 0 and vencedor== ' ':
            visual = jogadaHumana(nomes, visual)
            vencedor = verificaVencedor(visual)
            i += 1
        if (not i>=9+a) and vencedor==' ':
            visual = jogadaComputador(nomes, visual)
            vencedor = verificaVencedor(visual)
        mostraTabuleiro(visual)
        i += 1
        if vencedor!=' ':
            if vencedor in nomes[0]:
                print('\nVencedor: %s' % nomes[0][0])
            if vencedor in nomes[1]:
                print('\nVencedor: %s' % nomes[1][0])
            break
    if vencedor == ' ':
        print('Deu velha')
    if jogarNovamente():
        break
    else:
        system('clear')