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
    JogadaComputador(c)
    mostrarTabuleiro()
    p=JogadaHumana(a,b)
else:
    if b == 'X':
        c = ' O '
    else:
        c = ' X '
    p=JogadaHumana(a,b)
    JogadaComputador(c)
    mostrarTabuleiro()
            
while not verificaVencedor(b,tabuleiro,a):
    if sort==0:
        if JogadaComputador(c):
            if JogadaHumana(a,b):
                mostrarTabuleiro()
            
    else:
        if JogadaHumana(a,b):
            if JogadaComputador(c):
               mostrarTabuleiro()
            
            

    #if not jogueNovamente():
        #break
                
    




    
    