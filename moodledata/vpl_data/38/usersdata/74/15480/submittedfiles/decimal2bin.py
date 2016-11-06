# -*- coding: utf-8 -*-
from __future__ import division

n = input('Digite o numero binario: ')

i = 1
cont = 0
d = 0


while n>=0.9:
    n = n/10
    cont = cont+1
l = cont
while l>=i:
    n = n*10
    j = n//1
    d = d+j*2**cont
    cont = cont-1
    n = n-j
    i=i+1
print('%d'% d)




