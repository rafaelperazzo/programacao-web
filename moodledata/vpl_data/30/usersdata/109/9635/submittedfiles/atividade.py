# -*- coding: utf-8 -*-
from __future__ import division
import math

n=input('Digite o valor de n:')
cont=0

for a in range (0,n,1):
    s=((1+a)/(n-a))
    cont=cont+5
print cont
