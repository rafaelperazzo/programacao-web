# -*- coding: utf-8 -*-
from __future__ import division
a=int(input('digite o valor de um número:'))
s = 0
p = a
cont = 0
while p>0:
    p = p//2
    cont = cont + 1
d = 0
for i in range(0, cont, 1):
    b=a%2
    d = d + b*(10)**i
    a=a//2
print(d)
    
    

