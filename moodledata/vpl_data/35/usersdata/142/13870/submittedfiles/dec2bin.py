# -*- coding: utf-8 -*-
from __future__ import division

p=int(input('p:'))
q=int(input('q:'))
cont=0
x=p
while x>1:
    x=x//10
    cont=cont+1
    
h=0
while q>=1:
    if q%(10-cont)==p:
        h=h+1
        break
    q=q//10
if h>0:
    print('S')
else:
    print('N')