# -*- coding: utf-8 -*-
from __future__ import division

a=input('Digite o valor de a:')
cont=0

while a//2!=0:
    cont=cont+1
    a=a//2
    n=cont

k=0
m=0
while k<=n:
    r=((a%2)*10**k)
    k=k+1
    a=a//2
    m=m+r
print m


