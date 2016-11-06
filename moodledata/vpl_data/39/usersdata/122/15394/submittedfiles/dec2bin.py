# -*- coding: utf-8 -*-
from __future__ import division

a=input('Digite o valor de a:')

i=0
j=1
d=a%2

while a>0:
    d=a%2
    a=a//2
    i=i+d*j
    j=j*10
print ("%d"%i)


