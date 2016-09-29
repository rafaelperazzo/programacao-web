# -*- coding: utf-8 -*-
from __future__ import division
import math

#entrada
v = int(input('digite o valor em reais:'))
#processamento
n20 = v//20
n10 = v//(v%20)
n5 = v//(v//(v%20))
n2 = v//(v//(v//(v%20)))
n1 = v//(v//(v//(v//(v%20))))

#saida
print(n20)
print(n10)
print(n5)
print(n2)
print(n1)

