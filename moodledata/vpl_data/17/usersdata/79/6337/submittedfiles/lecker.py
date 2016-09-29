# -*- coding: utf-8 -*-
from __future__ import division
import math

#Entrda

a = float(input('Digite valor de "a": '))
b = float(input('Digite valor de "b": '))
c = float(input('Digite valor de "c": '))
d = float(input('Digite valor de "d": '))

#Processamento

if a < b > c > d or a > b > c > d or a < b < c > d or a < b > c < d:
    print('S')

else:
    print('N')
        

