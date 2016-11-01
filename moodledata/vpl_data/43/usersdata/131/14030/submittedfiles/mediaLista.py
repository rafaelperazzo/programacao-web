# -*- coding: utf-8 -*-
from __future__ import division

n = input('digite o valor de n:')

l=[] 
for i in range (0,n,1):
    l.append(input('digite o valor do elemento'))
    
print('%.2f'% l[0])
print(l[4])
print((sum(l))/n)
print l

