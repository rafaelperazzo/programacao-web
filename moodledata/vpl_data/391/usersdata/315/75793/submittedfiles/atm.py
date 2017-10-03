# -*- coding: utf-8 -*-
from __future__ import division
import math

#COMECE SEU CODIGO AQUI
a = int(input('valor a ser sacado: '))

c20 = a/20
c10 = a - (c20*20)
c5 = a - (c20*20) - (c10*10)
c2 = a - (c20*20) - (c10*10) - (c5*5)
c1 = a - (c20*20) - (c10*10) - (c5*5) - (c2*2)
print ('%d' %c20)
print ('%d' %c10)
print ('%d' %c5)
print ('%d' %c2)
print ('%d' %c1)
