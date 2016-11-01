# -*- coding: utf-8 -*-
from __future__ import division

p=input('digite p:')
q=input('digite q:')

cont=0
a=p
while p>0:
    p=p//10
    cont=cont+1
p=a
sub=0
while q>0:
    ulti=q%(10**cont)
    if ulti==p:
        sub=sub+1
        break
    else:
        q=q//10
   
if sub==0:
    print('N')
else:
    print('S')