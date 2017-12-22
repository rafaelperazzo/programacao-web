# -*- coding: utf-8 -*-

from minha_bib import *


# COLOQUE SEU PROGRAMA A PARTIR DAQUI
jgnov = 'S'
while jgnov == 'S' or jgnov =='s':
    print('Bem vindo ao JogoDaVelha do grupo D [Anderson Bezerra, Caio César, Laura, Juan]')
    nome = input('\nQual o seu nome (ou apelido)? ')
    jogador = 2
    smbH = 0
    smbH = solicitaSimbolodoHumano(smbH)
    
    if smbH == ' X ':
        smbPC = ' O '
    else:
        smbPC = ' X '
    
    
    jogador = sorteioPrimeiraJogada(jogador, nome)
    
    
    tabuleiro = [
        ['   ','   ','   '],
        ['   ','   ','   '],
        ['   ','   ','   ']
        ]
    
    
    som = 0
    while True:
        if jogador == 1:
            while True:
                JogadaHumana(smbH,tabuleiro, nome)
                break
            
            if verificaVencedor(smbH, tabuleiro, som):
                if verificaVencedor(smbH, tabuleiro, som) == 20:
                    mostraTabuleiro(tabuleiro)
                    print ('\nDeu Velha')
                    break
                else:
                    mostraTabuleiro(tabuleiro)
                    print('\nVencedor: %s'%nome)
                    break
            
            jogador = 0
        
        
        else:
            tabuleiro = JogadaComputador(smbPC,tabuleiro)
            
            if verificaVencedor(smbPC, tabuleiro, som):
                if verificaVencedor(smbPC, tabuleiro, som) == 20:
                    mostraTabuleiro(tabuleiro)
                    print ('\nDeu Velha')
                    break
                else:
                    mostraTabuleiro(tabuleiro)
                    print ('\nVencedor: Computador')
                    break
            
            
            jogador = 1

    jgnov = input('\nQuer jogar denovo? ')
    if jgnov == 'S' or jgnov == 's' or jgnov == 'SIM' or jgnov == 'sim':
        os.system('clear')
