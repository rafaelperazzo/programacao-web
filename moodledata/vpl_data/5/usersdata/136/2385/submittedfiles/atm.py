# -*- coding: utf-8 -*-
from __future__ import division
import math

#COMECE SEU CODIGO AQUI
a = int(input('Valor do saque:'))
n20 = int(a/20)
n10 = int(a%20)/10
n5 = int((a%20)%10)/5


print(n20)
print(n10)
print(n5)