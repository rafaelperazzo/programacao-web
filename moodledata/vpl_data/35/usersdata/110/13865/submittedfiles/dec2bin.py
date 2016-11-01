# -*- coding: utf-8 -*-
from __future__ import division
p=input('Digite p: ')
q=input('Digite q: ')
cont=0
a=p
while p>=1 :
    cont=cont+1
    p=p/10
i=10**cont
b=q
while b>=p:
    r=b%i
    if r==p:
        print('S')
    b=b/10
if b<q:
    print('N')
