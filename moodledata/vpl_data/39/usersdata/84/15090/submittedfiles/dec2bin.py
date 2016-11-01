# -*- coding: utf-8 -*-
from __future__ import division

b=input('digite o valor:')
a=b
n=0
contador=0
d=0

while n<a:
    a=a//2
    contador=contador+1
    
while n<contador:
    c=b%2
    b=b//2
    d=d+(c*(10**n))
    n=n+1
    
print (d)