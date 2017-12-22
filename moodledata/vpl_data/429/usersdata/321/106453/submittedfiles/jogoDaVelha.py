# -*- coding: utf-8 -*-
from jogoDaVelha_BIB import *

# COLOQUE SEU PROGRAMA A PARTIR DAQUI
print('Bem vindo ao JogoDaVelha do grupo 8 [Iara, Ingrid, Luiz Otávio, Tatiane]\n')

a=nome()

b=solicitaSimboloDoHumano()



while not verificaVencedor(b,tabuleiro,a):
    sort=sorteioPrimeiraJogada(a)
    if sort==0:
        if b == 'X':
            b = ' O '
        else:
            b = ' X '
        jogadaComputador(b)
        
    else:
        p=JogadaHumana(a)
        linha=p[0]
        coluna= p[1]
        tabuleiro[linha][coluna]= ' '+b+' '

    mostrarTabuleiro()
    validaJogada(nome,tabuleiro




    
    