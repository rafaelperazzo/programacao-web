# -*- coding: utf-8 -*-
from __future__ import division
a=input('Digite o valor de A; Lembre que, se o valor inserido for positivo, será calculado o seu quadrado, caso contrário será calculada sua raíz' :')
if a<0:
    x1=a**2
    print('Depois de processado, o valor inserido resulta em %.2f'%x1)
else:
    x2=a**0.5
    print('Depois de processado, o valor inserido resulta em %.2f'%x2)
    