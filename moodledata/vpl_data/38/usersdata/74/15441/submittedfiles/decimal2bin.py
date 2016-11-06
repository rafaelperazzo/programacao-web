# -*- coding: utf-8 -*-
from __future__ import division

n = input('Digite o numero binario: ')

k = n
cont = 0
d = 0

while n>=2:
    n = n/10
    cont = cont+1
d = 2**cont
    
while n>=1.1:
    n = n*10
    j = n//1
    d = d+j*2**cont
    cont = cont-1
    n = n-j
print('%d'% d)


