# -*- coding: utf-8 -*-
from __future__ import division
n=input('Digite o valor: ')
cont=0
d=n
while d>=1:
    d=d//10
    cont=cont+1
i=0
s=0
while n>=1:
    s=s+n%2*(10**i)
    i=i+1
    n=n//2
print(s)
    
