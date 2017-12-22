# -*- coding: utf-8 -*-
from minha_bib import *

#COMECE AQUI ABAIXO
"""
matriz = [
    ['   ','   ','   '],
    ['   ','   ','   '],
    ['   ','   ','   ']
    ]

print (matriz[0][0] + '|' + matriz[0][1] + '|' + matriz[0][2])
print (matriz[1][0] + '|' + matriz[1][1] + '|' + matriz[1][2])
print (matriz[2][0] + '|' + matriz[2][1] + '|' + matriz[2][2])

while 1:
    n = input('digite')
  
    
    matriz[int(n[0])][int(n[2])] = ' X '
    
    print (matriz[0][0] + '|' + matriz[0][1] + '|' + matriz[0][2])
    print (matriz[1][0] + '|' + matriz[1][1] + '|' + matriz[1][2])
    print (matriz[2][0] + '|' + matriz[2][1] + '|' + matriz[2][2])
    print('vez do pc')
    JogadaComputador(matriz)
    print (matriz[0][0] + '|' + matriz[0][1] + '|' + matriz[0][2])
    print (matriz[1][0] + '|' + matriz[1][1] + '|' + matriz[1][2])
    print (matriz[2][0] + '|' + matriz[2][1] + '|' + matriz[2][2])
    if ganhou(' X ',matriz):
        print('Cabo')
        break


"""













print('Bem vindo ao JogoDaVelha do grupo D [Anderson Bezerra, Caio César]')
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
        if verificaVencedor(smbH, tabuleiro):
            print('\nVencedor: %s'%nome)
            break
        jogador = 0
    
    
    else:
        tabuleiro = JogadaComputador(smbPC,tabuleiro)
        if verificaVencedor(smbPC, tabuleiro):
            print ('\nVencedor: Computador')
            break
        
        jogador = 1
