# -*- coding: utf-8 -*-
from __future__ import division
import math
#COMECE SEUCÓDIGO AQUI
L=int(input('Digite o valor do jogador que lança a bola:'))
R=int(input('Digite o valor do jogador que recebe a bola:'))
D=int(input('Difite o valor do último jogador do time adversário:'))
if(R>50 and R>L and R>D):
    print('S')
else:
    print('N')
    