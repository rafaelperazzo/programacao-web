# -*- coding: utf-8 -*-
from __future__ import division
p = input('digite um valor de p:')
q = input('digite um valor de q:')
cont = 0
c = p
while c>=1:
    c =c//10
    cont = cont +1
cont2 = 0
while q>0:
    if q%(10**cont)==p:
        cont2=cont2+1
    q=q//10
if cont2>0:
    print 'N'
else:
    print 'S'
