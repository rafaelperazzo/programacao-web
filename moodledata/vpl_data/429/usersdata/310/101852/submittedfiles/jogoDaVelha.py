# -*- coding: utf-8 -*-
from jogoDaVelha_BIB import *

# COLOQUE SEU PROGRAMA A PARTIR DAQUI



print('Bem vindo ao JogoDaVelha do grupo D [Anderson Bezerra, Caio César, Juan]')
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



while True:
    if jogador == 1:
        while True:
            JogadaHumana(smbH,tabuleiro, nome)
            break
        jogador = 0
    
    
    else:
        tabuleiro = JogadaComputador(smbPC,tabuleiro)
        jogador = 1