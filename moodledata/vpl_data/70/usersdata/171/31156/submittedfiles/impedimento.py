# -*- coding: utf-8 -*-
import math
l=float(input('digite a distancia ate o gol adversario em que o jogador lancou a bola:'))
r=float(input('digite a distancia ate o gol adversario em qu o jogador recebe a bola:'))
d=float(input('digite a distancia em que o ultimo defensor esta de seu gol:'))
if r>50 and l<r and r>d:
    print('S')
else:
    print('N')