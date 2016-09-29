# -*- coding: utf-8 -*-
from __future__ import division
A=input('Digite o peso da primeira esfera: ')
B=input('Digite o peso da segunda esfera: ')
C=input('Digite o peso da terceira esfera: ')
D=input('Digite o peso da quarta esfera: ')

if (A==B+C+D and B+C==D and B==C):
    print('S')
    
else:
    print('N')