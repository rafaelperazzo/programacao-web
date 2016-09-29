# -*- coding: utf-8 -*-
from __future__ import division
import math
#COMECE SEU CÓDIGO AQUI

L=input('Digite a posição do atacante que lança a bola:')
R=input('Digite a posição do jogador atacante que recebe a bola:')
D=input('Digite a posição do último jogador defensor:')

if R>50 and L<R and R>D:
    print('N')
else:
    print('S')