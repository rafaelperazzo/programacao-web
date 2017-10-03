# -*- coding: utf-8 -*-
from __future__ import division
import math

#COMECE SEU CODIGO AQUI
a = int(input('Valor do saque: R$ '))
b = (a//20)
c = (a%20)
d = (c//20)
e = (c%20)
f = (e//20)
g = (e%20)
h = (g//20)
i = (g%20)
j = (i//20)
k = (i%20)
print('{}\n{}\n{}\n{}\n{}\n'.format(b,d,f,g,j))