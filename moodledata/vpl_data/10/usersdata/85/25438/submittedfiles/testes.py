# -*- coding: utf-8 -*-
from __future__ import division

d= input('Digite o valor de d: ')
n= input('Digite o valor de n: ')

r= d%2
soma=0
for i in range(0,n,1):
    soma=soma+(r*(10**i)
    d= d//2
    r= d%2
    
print soma