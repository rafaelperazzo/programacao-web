# -*- coding: utf-8 -*-
from __future__ import division
import math

#COMECE SEU CODIGO AQUI
a = int(input('valor a ser sacado: '))

c20 = int(a/20)
c10 = int((a - (c20*20))/10)
c5 = int((a - (c20*20) - (c10*10))/5)
c2 = int((a - (c20*20) - (c10*10) - (c5*5))/2)
c1 = int(a - (c20*20) - (c10*10) - (c5*5) - (c2*2))
print ('%d' %c20)
print ('%d' %c10)
print ('%d' %c5)
print ('%d' %c2)
print ('%d' %c1)
