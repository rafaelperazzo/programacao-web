# -*- coding: utf-8 -*-
from __future__ import division
import math

#Entrda

a = float(input('Digite valor de "n1": '))
b = float(input('Digite valor de "n2": '))
c = float(input('Digite valor de "n3": '))
d = float(input('Digite valor de "n4": '))

#Processamento

if a < b > c > d or a > b > c > d or a > b < c > d or a > b > c < d:
    print('S')

else:
    print('N')
        

