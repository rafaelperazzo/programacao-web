# -*- coding: utf-8 -*-
from __future__ import division
import math
valor=int(input('digite o valor:'))
if valor>0:
    n20=valor/20
    n10=(valor%20)/10
    n5=((valor%20)%10)/5
    n2=(((valor%20)%10)%5)/2
    n1=((((valor%20)%10)%5)%2)/1
print('%d' %n20)
print('%d' %n10)   
print('%d' %n5)
print('%d' %n2)
print('%d' %n1)