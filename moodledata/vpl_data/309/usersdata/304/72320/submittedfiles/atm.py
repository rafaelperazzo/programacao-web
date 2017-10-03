# -*- coding: utf-8 -*-
from __future__ import division
import math

#COMECE SEU CODIGO AQUI
a = int(input('Valor do saque: R$ '))
b = (a//20)
c = (a%20)
d = (c//10)
e = (c%10)
f = (e//5)
g = (e%5)
h = (g//2)
i = (g%2)
j = (i//1)
k = (i%1)
print('{}\n{}\n{}\n{}\n{}\n'.format(b,d,f,h,j))
