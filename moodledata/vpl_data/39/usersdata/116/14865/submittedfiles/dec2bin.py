# -*- coding: utf-8 -*-
from __future__ import division

n = input ('insira o valor de n:')
cont=0
i=0
while n>0:
    a=n%2
    cont= cont+a*(10**i)
    n=n//2
    i=i+1
print (cont)