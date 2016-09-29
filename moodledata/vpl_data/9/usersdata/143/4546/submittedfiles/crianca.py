# -*- coding: utf-8 -*-
from __future__ import division
p1 = input(' Peso da Criança 1: ')
c1 = input(' Comprimento da parte esquerda da gangorra: ')
p2 = input(' Peso da Criança 2: ')
c2 = input(' Comprimento da parte direita da gangorra: ')

torque = p1*c1-p2*c2
if torque<0 :
    print(' 1 ')
elif torque>0 :
    print(' -1 ')
else:
    print(' 0 ')