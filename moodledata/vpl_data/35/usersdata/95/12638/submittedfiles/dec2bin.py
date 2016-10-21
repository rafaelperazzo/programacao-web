# -*- coding: utf-8 -*-
from __future__ import division

p=int(input('Digite p:'))
q=int(input('Digite q:'))
contp=contq=cont=0
k=p
while k>0:
    k=k//10
    contp+=1
np=contp

w=q
while w>0:
    w=w//10
    contq+=1
nq=contq

if np<=nq:
    a=10**np
    while q>0:
        if q%a==p:
            cont+=1
            break
if cont>0:
    print('S')
else:
    print('N')