# -*- coding: utf-8 -*-
from __future__ import division
import math

#COMECE SEU CODIGO AQUI
v = int(input('Valor a ser sacado: ' ))

c20 = v//20
c10 = (v - (c20*20))//10
c5 = (v - (c20*20) - (c10*10))//5
c2 = (v - (c20*20) - (c10*10) - (c5*5))//2
c1 = v - (c20*20) - (c10*10) - (c5*5) - (c2*2)

print('%d' %c20)
print('%d' %c10)
print('%d' %c5)
print('%d' %c2)
print('%d' %c1)
