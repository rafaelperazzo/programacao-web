# -*- coding: utf-8 -*-
from __future__ import division
import math

n1 = int(input('Digite o valor do primeiro número:'))
n2 = int(input('Digite o valor do segundo número:'))
contdiv=0
mdc = n2
while (n1%n2) >0:
    if n1%n2 != 0 :
        contdiv = contdiv +1
    else:
        n1 = n2 and n2 = (n1%n2)
    
    
   
print(mdc)
print(contdiv)