# -*- coding: utf-8 -*-
from __future__ import division
import math

n1 = int(input('Digite o valor do primeiro número:'))
n2 = int(input('Digite o valor do segundo número:'))
contdiv=0

while True:
    if (n1%n2) > 1:
        contdiv = contdiv + 1
    
    else:
        break
    n1 = n2
    n2 = (n1%n2)
print(contdiv)