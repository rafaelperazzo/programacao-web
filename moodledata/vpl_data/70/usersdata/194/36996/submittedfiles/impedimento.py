# -*- coding: utf-8 -*-
import math
L=float(input('digite a posição do jogador atacante que lança a bola :'))
R=float(input('digite a posição do jogador atacante que recebe a bola:'))
D=float(input('digite a posição do ultimo jogador defensor:'))
if R>50 and L<R and R>D:
    print('5')
else:
        print('N')