# -*- coding: utf-8 -*-
from __future__ import division

b=input('Digite o valor de b:')
cont=2

while b//10!=1:
    cont=cont+1
    b=b//10
    n=cont


m=0
k=0

while k<=n-1:
    (b%10)*2**k
    b=b//100
    k=k+1
    m=m+((b%100)*2**k)
print m




