# -*- coding: utf-8 -*-
from __future__ import division
import math

#COMECE SEU CODIGO AQUI
n=int(input('digite o valor que deseja sacar:'))
a=math.floor(n/20)
b=n-20*a
b1=math.floor(b/10)
c=b-10*b1
c1=math.floor(c/5)
d=c-5*c1
d1=math.floor(d/2)
e=d-2*d1
print('%d' %a)
print('%d' %b1)
print('%d' %c1)
print('%d' %d1)
print('%d' %e)