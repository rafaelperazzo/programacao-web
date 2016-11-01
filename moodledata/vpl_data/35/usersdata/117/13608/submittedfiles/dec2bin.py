# -*- coding: utf-8 -*-
from __future__ import division

p=input('digite p:')
q=input('digite q:')

cont=0
a=p
wile p>0:
    p=p//10
    cont=cont+1
p=a
sub=0
while q>0:
    ulti=q%(10**cont)
    if ulti==p:
        sub=bub+1
        break
    else:
        q=q//10