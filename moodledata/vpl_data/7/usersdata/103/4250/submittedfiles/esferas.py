# -*- coding: utf-8 -*-
from __future__ import division
A=input('Insira o peso da primeira esfera:')
B=input('Insira o peso da segunda esfera:')
C=input('Insira o peso da terceira esfera:')
D=input('Insira o peso da quarta esfera:')
if A==B+C+D and B==C and B+C==D:
    print('S')
else:
    print('N')
