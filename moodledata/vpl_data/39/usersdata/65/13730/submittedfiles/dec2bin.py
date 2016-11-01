# -*- coding: utf-8 -*-
from __future__ import division

d=input('Digite d: ')

a=d
i=0
contador=0
b=0

while i<a:
    a=a//2
    contador=contador+1
    
while i<contador:
    n=d%2
    d=d//2
    b=b+(n*(10**i))
    i=i+1
    
print(b)