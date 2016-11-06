# -*- coding: utf-8 -*-
from __future__ import division

n= int(input('Digite o valor de n: '))
p=n
cont=0
while p>0:
    p=p//2
    cont=cont+1
d=0
for i in range(0,cont,1):
    b=a%2
    d=d+b*(10**i)
    a=a//2
print d