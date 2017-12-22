# -*- coding: utf-8 -*-
from jogoDaVelha_BIB import *

# COLOQUE SEU PROGRAMA A PARTIR DAQUI
print('Bem vindo ao JogoDaVelha do grupo 8 [Iara, Ingrid, Luiz Otávio, Tatiane]\n')

a=nome()

b=solicitaSimboloDoHumano()

sort=sorteioPrimeiraJogada(a)


    
if sort==0:
    if b == 'X':
        b = ' O '
    else:
        b = ' X '
    jogadaComputador(b)
    mostrarTabuleiro()
else:
    if b == 'X':
        b = ' O '
    else:
        b = ' X '
    p=JogadaHumana(a,b)
    jogadaComputador(b)
    mostrarTabuleiro()
            
while not verificaVencedor(b,tabuleiro,a):
    if sort==0:
        if b == 'X':
            b = ' O '
        else:
            b = ' X '
        jogadaComputador(b)
        p=JogadaHumana(a,b)
    else:
        if b == 'X':
            b = ' O '
        else:
            b = ' X '
        p=JogadaHumana(a,b)
        jogadaComputador(b)
    
    mostrarTabuleiro()
    validaJogada(nome,tabuleiro)




    
    