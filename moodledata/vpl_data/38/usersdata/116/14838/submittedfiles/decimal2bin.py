# -*- coding: utf-8 -*-
from __future__ import division

n=input ('insira n:')

cont=0
c=0
while n>0:
    a=n%(10**i)
    b=a*(2**c)
    cont = cont+b
    n=n//10
    c=c+1
    
    