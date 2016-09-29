# -*- coding: utf-8 -*-
from __future__ import division
import math

#COMECE SEU CODIGO AQUI
a = input('Digite o valor em reais: ')
b = a//20
c = (a - (b*20))//10
d = (a - (c*10)+(b*20))//5
e = (a - (d*5)+(c*10)+(b*20))//2
f = (a - (e*2)+(d*5)+(c*10)+(b*20))
print('%d, %d, %d, %d, %d' %b,c,d,e,f)