# -*- coding: utf-8 -*-
from __future__ import division
p = input('digite um valor de p:')
q = input('digite um valor de q:')
cont = 0
c = q
while c>=1:
    c =c//10
    cont = cont +1
cont2 = 0
while p>0:
    if p%(10**cont)==q:
        cont2=cont2+1
    p=p//10
if cont2>0:
    print 'S'
else:
    print 'N'
