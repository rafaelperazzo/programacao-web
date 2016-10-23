# -*- coding: utf-8 -*-
from __future__ import division

p= int(input('digite p:'))
q= int(input('digite q:'))
cont=0
while p>1:
    p=p//10
    cont=cont+1
p=p*(10**cont)
h=0

while q>=1:
   if q%(10**cont)==p:
        h=h+1
   
    q=q//10
if h>0:
    print('S')
else:
    print('N')