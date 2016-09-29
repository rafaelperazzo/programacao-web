# -*- coding: utf-8 -*-
from __future__ import division
import math
L=int(input('Digitar o valor do jogador que lança a bola:'))
R=int(input('Digitar o valor do jogador que recebe a bola:'))
D=int(input('Digitar o valor do último jogador do time adversário:'))
if(R>50 and R>L and R>D):
    print('S')
else:
    print('N')