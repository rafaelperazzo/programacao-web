# -*- coding: utf-8 -*-
from __future__ import division
import math

L=input('digite a posição de L:')
R=input('digite a posição de R:')
D=input('digite a posição de D:')

if (R>50)and(L<R)and(R>D):
    print('S')
else:
    print('N')