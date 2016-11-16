# -*- coding: utf-8 -*-
from __future__ import division

n = input ('Digite n:')
a = []

for i in range (0,n,1):
    a.append (input ('Digite um elemento de a:'))
    
m = input ('Digite m:')
b = []

for i in range (0,m,1):
    b.append (input ('Digite um elemento de b:'))
    
cont = 0
for i in range (0,len(m),1):
    if b[i] in a:
        cont = cont +1

print (cont)