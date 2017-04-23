# -*- coding: utf-8 -*-
import math
L=int(input('digite a posição do jogador atacante que lança a bola: '))
R=int(input('digite a posição do jogador atacante que recebe a bola: '))
D=int(input('digite a posição do ultimo jogador defensor: '))
if R>50 and L<R and R>D:
    print('S')
else:
        print('N')