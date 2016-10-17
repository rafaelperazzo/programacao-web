# -*- coding: utf-8 -*-
from __future__ import division
import math

#Entrada

n=input('Digite n: ')
while n%2 != 0:
    n=input('Digite n: ')
    
x1=input('Digite X1: ')
y1=input('Digite Y1: ')
x2=input('Digite X2: ')
y2=input('Digite Y2: ')

#Processamento

mx=(n/2)
my=(n/2)

if x1<=mx and x2>mx:
    print('S')

elif x1>mx and x2<=mx:
    print('S')

elif y1<=my and y2>my:
    print('S')

elif y1>my and y2<=my:
    print('S')

else:
    print('N')