# -*- coding: utf-8 -*-
from __future__ import division
import math

L = input ('Digite a posição do jogador atacante que lança a bola:')
R = input ('Digite a posição do jogador atacante que recebe a bola:')
D = input ('Digite a posição do jogador defensor:')

if ((R>20) and (L<R) and (R>D)):
    print ('S')
else:
    print ('N')
    