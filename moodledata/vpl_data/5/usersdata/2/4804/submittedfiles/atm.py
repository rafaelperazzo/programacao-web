# -*- coding: utf-8 -*-
from __future__ import division
import math

#COMECE SEU CODIGO AQUI

total = int(input('Digite o valor total: '))

t20 = total // 20
total = total % 20

t10 = total // 10
total = total % 10

t5 = total // 5
total = total % 5

t2 = total // 2
total = total % 2

t1 = total // 1
total = total % 1

print t20
print t10
print t5
print t2
print t1