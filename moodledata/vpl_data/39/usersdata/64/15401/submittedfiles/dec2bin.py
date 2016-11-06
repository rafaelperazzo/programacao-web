# -*- coding: utf-8 -*-
from __future__ import division

a = int(input("Digite o número: "))

cont = 1

while a//2 !=0:
    cont = cont +1
    a = a//2
    n = cont
    
x = 0
m = 0

while x <= n-1:
    r = (a%2)*(10**x)
    
    x=x+1
    a = a//2
    
    m = m+r
    
print m
print n
