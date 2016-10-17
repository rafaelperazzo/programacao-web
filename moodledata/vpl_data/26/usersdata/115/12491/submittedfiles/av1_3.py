# -*- coding: utf-8 -*-
from __future__ import division
import math

a=input('digite o valor inteiro:')
b=input('digite o valor real:')
cont1 = 1
cont2 = 0
c = 1
d = 10
e = 0.11
f = 1
g = 0
while  a>=c:
    if a/d>=1:
        cont1 = cont1+1
    d=d*10
    c=c+1
print ('%d'% cont1)
while b>=e:
    g=g+1
    f=f*10
    e=e*(1/f)
    a=b*10
    b=(a/10-b)
print ('%d'% cont2) 
