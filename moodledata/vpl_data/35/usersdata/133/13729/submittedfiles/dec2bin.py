# -*- coding: utf-8 -*-
from __future__ import division
p = int(input('Digite o valor de p:'))
q = int(input('Digite o valor de q:'))

i = 0
while(q>=1):
    q = q//10
    i = i+1
a = 0
while(p>0):
    if(p%(10**i) == q):
        a = a +1
        break
    p = p//10
if(a>0):
    print('S')
else:
    print('N')