# -*- coding: utf-8 -*-
from __future__ import division
import math
#1
L = input('Digite o valor da posição de L(entre 0 e 100 m) =')
R = input('Digite o valor da posição de R(entre 0 e 100 m) =')
D = input('Digite o valor da posição de D(entre 0 e 100 m) =')

#2
if R>50 and L<R and R>D:
    print('S')
else :
    print('N')