# -*- coding: utf-8 -*-
from __future__ import division

p=int(input('digite p:'))
q=int(input('digite q:'))

contp=0
contq=0
cont=0
x=p
while x>0:
    x=x//10
    contp=contp+1
np=contp

y=q
while y>0:
    y=y//10
    contq=contq+1
nq=contq

if np<=nq:
    a=10**np
    while q>0:
        if q%a==p:
            cont=cont+1
            break
        q=q//10
if cont>0:
    print('S')
else:
    print('N')