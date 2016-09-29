# -*- coding: utf-8 -*-
from __future__ import division
import math
#ENTRADA
l=input ('digite a posição do jogador l:')
r=input ('digite a posição do jogador r:')
d=input ('digite a posição do jogador d:')

#SAIDA
if r>50 and l<r and r>d:
    print ('S')
else:
    print ('N')