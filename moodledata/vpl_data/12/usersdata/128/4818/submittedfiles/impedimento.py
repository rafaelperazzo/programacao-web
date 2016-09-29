# -*- coding: utf-8 -*-
from __future__ import division
import math
#COMECE SEU CÓDIGO AQUI

l=input('Posição do jogadro L: ')
r=input('Posição do jogador R: ')
d=input('Posição do jogador D: ')

if r>50 and l<r and r>d:
    print ('S')

else:
    print ('N')