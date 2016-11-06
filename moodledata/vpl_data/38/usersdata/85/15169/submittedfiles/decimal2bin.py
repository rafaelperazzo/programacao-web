# -*- coding: utf-8 -*-
from __future__ import division

n= int(input('Digite o valor de n: '))

b=n
cont=0
while b>0:
    b=b//10
    cont=cont+1
s=0
for i in range(0,cont,1):
    r=n%10
    a=r*(2**i)
    s=s+a
    n=n//10
print s