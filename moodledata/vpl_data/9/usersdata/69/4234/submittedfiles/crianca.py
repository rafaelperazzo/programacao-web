# -*- coding: utf-8 -*-
from __future__ import division
p1=input('digite o peso da criança da direita:')
c1=input('digite o comprimento do lado direito da gangorra:')
p2=input('digite o peso da criança da esquerda:')
c2=input('digite o comprimento do lado esquerdo da gangorra:')
if (p1*c1)==(p2*c2):
    print('0')
elif (p1*c1)<(p2*c2):
    print('-1')
else:
    print('1')