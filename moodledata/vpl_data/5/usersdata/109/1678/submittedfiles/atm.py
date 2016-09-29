# -*- coding: utf-8 -*-
from __future__ import division
import math

#COMECE SEU CODIGO AQUI
#20,10,5,2,1

c1 = input('Digite o valor que você quer sacar:')
d= c1*100
c = d//100

a20 = c//20
a20r = c%20
a10 = a20r//10
a10r = a20r%10
a5 = a10r//5
a5r = a10r%5
a2 = a5r//2
a2r = a5r%2
a1 = a2r//1

print a20
print a10
print a5
print a2
print a1

