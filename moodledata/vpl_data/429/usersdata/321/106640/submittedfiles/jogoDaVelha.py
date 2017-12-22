# -*- coding: utf-8 -*-
from jogoDaVelha_BIB import *

# COLOQUE SEU PROGRAMA A PARTIR DAQUI
print('Bem vindo ao JogoDaVelha do grupo 8 [Iara, Ingrid, Luiz Otávio, Tatiane]\n')

a=nome()

b=solicitaSimboloDoHumano()

sort=sorteioPrimeiraJogada(a)

if sort==0:
    if b == 'X':
        c = ' O '
    else:
        c = ' X '
    jogadaComputador(c)
    mostrarTabuleiro()
else:
    if b == 'X':
        c = ' O '
    else:
        c = ' X '
    p=JogadaHumana(a,b)
    jogadaComputador(c)
    mostrarTabuleiro()
            
while True:
    if sort==0:
        if jogadaComputador(c):
            if JogadaHumana(a,b):
                mostrarTabuleiro()
                verificaVencedor(b,tabuleiro,a)
    else:
        if JogadaHumana(a,b):
            if jogadaComputador(c):
                mostrarTabuleiro()
                verificaVencedor(b,tabuleiro,a)
    




    
    