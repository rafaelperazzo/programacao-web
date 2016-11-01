# -*- coding: utf-8 -*-
from __future__ import division
p=int(input('p:'))
q=int(input('q:'))
cont=0
a=p
while a>=1:
    a=a//10
    cont=cont+1
cont2=0
while q>0:
    if q%(10**cont)==p:
        cont2=cont2+1
        break
    q=q//10
if cont2>0:
    print('s')
else:
    print('n')


