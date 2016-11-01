# -*- coding: utf-8 -*-
from __future__ import division

b=input('digite o valor:')
c=b
n=0
contador=0
d=0

while n<c:
    c=c//10
    contador=contador+1
    
while n<contador:
    e=b%10
    b=b//10
    d=d+(e*(2**n))
    n=n+1
    
print(d)