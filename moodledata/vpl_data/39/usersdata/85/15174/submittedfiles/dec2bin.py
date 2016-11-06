# -*- coding: utf-8 -*-
from __future__ import division

n= int(input('Digite o valor de n: '))
p=n
cont=0
while p>0:
    p=p//2
    cont=cont+1
s=0
for i in range(0,cont,1):
    r=n%2
    a=r*(10**i)
    s=s+a
    n=n//2
print s