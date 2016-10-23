# -*- coding: utf-8 -*-
from __future__ import division

p= int(input('digite p:'))
q= int(input('digite q:'))
cont=0
while p>1:
    p=p/10
    cont=cont+1
p=p*(10**cont)
h=0
x=q
while q>1:
    if p==x:
        print('S')
    elif q%(10**cont)==p:
        h=1
        print('S')
    q=q//10
if h==0:
    print('N')