# -*- coding: utf-8 -*-
from jogoDaVelha_BIB import *

# COLOQUE SEU PROGRAMA A PARTIR DAQUI
print('Bem vindo ao JogoDaVelha do grupo 8 [Iara, Ingrid, Luiz Otávio, Tatiane]\n')

a=nome()

b=solicitaSimboloDoHumano()

sort=0

sorteioPrimeiraJogada(a)

if sort==0:
    jogadaComputador()
else:
    JogadaHumana(a)      



mostrarTabuleiro(tabuleiro)



validaJogada(tabuleiro,s)

tabuleiro = [
    ['  ','  ','  '],
    ['  ','  ','  '],
    ['  ','  ','  ']]
    

print(mostrarTabuleiro(tabuleiro))