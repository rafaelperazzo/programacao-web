# -*- coding: utf-8 -*-
from __future__ import division
p= input('digite p:')
q= input('digite q:')
cont=0

while p>0:
    if p%(10**cont)==q:
        print('N')
        break
    p=p//10
if cont>0:
    print('S')
else:
    print('N')

