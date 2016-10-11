# -*- coding: utf-8 -*-
from __future__ import division
import math

n=int(input('Digite o valor de n:'))
cont=0
while True:
    s=(n//10)
    cont=cont+1
    n=s
    if s<1:
     break
print cont

