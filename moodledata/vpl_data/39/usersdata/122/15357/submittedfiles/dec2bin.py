# -*- coding: utf-8 -*-
from __future__ import division

a=input('Digite o valor de a:')
cont=1

while a//2!=0:
    cont=cont+1
    a=a//2
    n=cont

k=0
m=0

while k<=n-1:
    (a%2)*10**k
    k=k+1
    a=a//2
    m=m+((a%2)*10**k)
print m