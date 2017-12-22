# -*- coding: utf-8 -*-
from jogoDaVelha_BIB import *

# COLOQUE SEU PROGRAMA A PARTIR DAQUI
print('Bem vindo ao JogoDaVelha do grupo 8 [Iara, Ingrid, Luiz Otávio, Tatiane]\n')

a=nome()

b=solicitaSimboloDoHumano()

sort=sorteioPrimeiraJogada(a)

if b == 'X':
    b = ' O '
else:
    b = ' X '
            
while not verificaVencedor(b,tabuleiro,a):
    
    if sort==0:
        jogadaComputador(b)
    else:
        p=JogadaHumana(a,b)
        
    
    

    mostrarTabuleiro()
    validaJogada(nome,tabuleiro)




    
    