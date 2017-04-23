# -*- coding: utf-8 -*-
import math
#COMECE SEU CÓDIGO AQUI
l=float(input('digite a posicao do jogador que lança:'))
r=float(input('digite a posicao do jogador que recebe:'))
d=float(input('digite a pposicao do jogador que defende:'))
if r>50 and l<r and r>d:
    print('s')
else:
    print('n')