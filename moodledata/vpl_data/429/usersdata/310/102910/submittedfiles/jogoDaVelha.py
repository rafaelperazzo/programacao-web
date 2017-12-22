# -*- coding: utf-8 -*-
from jogoDaVelha_BIB import *

# COLOQUE SEU PROGRAMA A PARTIR DAQUI

print('Bem vindo ao JogoDaVelha do grupo D [Anderson Bezerra, Caio César, Hugo Brendon, Juan]')
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
        if verificaVencedor(smbPC, tabuleiro, som) == 20:
            mostraTabuleiro(tabuleiro)
            print ('Velha')
            break
        if verificaVencedor(smbH, tabuleiro, som):
            mostraTabuleiro(tabuleiro)
            print('\nVencedor: %s'%nome)
            break
        jogador = 0
    
    
    else:
        tabuleiro = JogadaComputador(smbPC,tabuleiro)
        if verificaVencedor(smbPC, tabuleiro, som) == 20:
            mostraTabuleiro(tabuleiro)
            print ('Velha')
            break
        if verificaVencedor(smbPC, tabuleiro, som):
            mostraTabuleiro(tabuleiro)
            print ('\nVencedor: Computador')
            break
        
        jogador = 1