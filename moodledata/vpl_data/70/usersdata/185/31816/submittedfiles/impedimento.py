# -*- coding: utf-8 -*-
import math
L=float(input('digite a quantos metros o jogador atacante que lança a bola está do gol:'))
R=float(input('digite a quantos metros o jogador atacante que recebe a bola está do gol:'))
D=float(input('digite a quantos metros está o ultimo jogador defensor está do gol:'))
if R>50 and L<R and R>D:
    print('S')
else:
    print('N')