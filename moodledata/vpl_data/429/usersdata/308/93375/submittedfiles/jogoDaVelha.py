# -*- coding: utf-8 -*-
from jogoDaVelha_BIB import *

visual = [[' ',' ', ' '], [' ', ' ',' '], [' ', ' ', ' ']]  
nomes = [['', ''], ['Computador', '']]
print('Bem Vindo ao Jogo da Velha do Grupo "Deu Velha"')
nomes[0][0]=solicitaNomeDoJogador()
a=solicitaSimboloDoHumano()
nomes[0][1]=a[0]
nomes[1][1]=a[1]

i = sorteioPrimeiraJogada(nomes)
a = 0
while i<9+a:
    if i%2 == 0:
        visual = jogadaHumana(nomes[0], visual)
        i += 1
    if not i>=9+a:
        jogadaComputador(nomes[1], visual)
    mostraTabuleiro(i, visual)
    i += 1

print('Fim do jogo')
