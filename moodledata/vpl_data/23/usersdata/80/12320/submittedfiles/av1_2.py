# -*- coding: utf-8 -*-
from __future__ import division
import math

n=int(input('Digite as dimensoes da Barra:'))
x1=int(input('Digite o X1:'))
y1=int(input('Digite o Y1:'))
x2=int(input('Digite o X2:'))
Y2=int(input('Digite o Y2:'))
if x1<=(n/2) and x2>(n/2):
    print('S')
elif y1<=(n/2) and y2>(n/2):
    print('S')
else:
    print('N')