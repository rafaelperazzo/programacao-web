# -*- coding: utf-8 -*-
from __future__ import division

b=input('Digite b: ')

a=b
i=0
d=0
contador=0

while i<a:
    a=a//10
    contador=contador+1
    
while i<contador:
    
    n=b%10
    b=b//10
    d=d+(n*(2**i))
    i=i+1

print(d)