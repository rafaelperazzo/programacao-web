# -*- coding: utf-8 -*-
from jogoDaVelha_BIB import *

# COLOQUE SEU PROGRAMA A PARTIR DAQUI
print('Bem vindo ao JogoDaVelha do grupo 8 [Iara, Ingrid, Luiz Otávio, Tatiane]\n')

a=nome()

b=solicitaSimboloDoHumano()

sort=0
computador=''

sorteioPrimeiraJogada(a)

if sort==0:
    print(tabuleiro[jogadaComputador()])
    
else:
    JogadaHumana(a)      


tabuleiro = [
    ['  ','  ','  '],
    ['  ','  ','  '],
    ['  ','  ','  ']]

mostrarTabuleiro(tabuleiro,computador)



validaJogada(tabuleiro,computador)



