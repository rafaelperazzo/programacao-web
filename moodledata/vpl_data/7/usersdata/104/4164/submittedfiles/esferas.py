# -*- coding: utf-8 -*-
from __future__ import division
#ENTRADA
A=input('Digite o valor de A:')
B=input('Digite o valor de B:')
C=input('Digite o valor de C:')
D=input('Digite o valor de D:')
#PROCESSAMENTO
y=(B+C+D)
x=(B+C)
if A==y and D==x and B==C:
    print('S')
else:
    print('N')