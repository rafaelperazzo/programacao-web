# -*- coding: utf-8 -*-
from jogoDaVelha_BIB import *

visual = [[' ',' ', ' '], [' ', ' ',' '], [' ', ' ', ' ']]  

print('Bem Vindo ao Jogo da Velha do Grupo "Deu Velha"')
nomes[0][0]=solicitaNomeDoJogador()
a=solicitaSimboloDoHumano()
nomes[0][1]=a[0]
nomes[1][1]=a[1]
print(nomes)
