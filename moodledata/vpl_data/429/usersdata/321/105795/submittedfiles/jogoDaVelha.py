# -*- coding: utf-8 -*-
from jogoDaVelha_BIB import *

# COLOQUE SEU PROGRAMA A PARTIR DAQUI
print('Bem vindo ao JogoDaVelha do grupo 8 [Iara, Ingrid, Luiz Otávio, Tatiane]\n')


a=nome()

b=solicitaSimboloDoHumano()




sort=sorteioPrimeiraJogada(a)
if sort == 1:
    print ('Vencedor do sorteio para início do jogo: %s' % j1)
if sort == 0:
    print ('Vencedor do sorteio para início do jogo: %s' % j2)



if sort==0:
    jogadaComputador(b)
    
else:
    JogadaHumana(a)      

tabuleiro = [
    ['  ','  ','  '],
    ['  ','  ','  '],
    ['  ','  ','  ']]

mostrarTabuleiro()

validaJogada(tabuleiro)



