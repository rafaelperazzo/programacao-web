# -*- coding: utf-8 -*-
from __future__ import division
import math

v = int(input('Digite o valor a ser sacado:'))
c1 = v/20
c2 = (v%20)/10
c3 = ((v%20)%10)/5
c4 = (((v%20)%10)%5)/2
c5 = ((((v%20)%10)%5)%2)/1
print('%d'%c1)
print('%d'%c2)
print('%d'%c3)
print('%d'%c4)
print('%d'%c5)
