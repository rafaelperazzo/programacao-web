# -*- coding: utf-8 -*-
from __future__ import division

n= input( )
x=[]
for i in range(0, n, 1):
    x.append(input( ))
y=[]
for i in range(0, n, 1):
    y.append(input( ))

mediax= 0
for i in range(0, n, 1):
    mediax= mediax+ x[i]
mediax= mediax/n

mediay= 0
for i in range(0, n, 1):
    mediay= mediay+ y[i]
mediay= mediay/n

p= 0
for i in range(0, n, 1):
    p= p+ (x[i]-mediax)*(y[i]-mediay)

p= p/(p**(1/2))

print p
