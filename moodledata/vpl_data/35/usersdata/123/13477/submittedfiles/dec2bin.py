# -*- coding: utf-8 -*-
from __future__ import division
p=input('Insira p:')
q=input('Insira q:')
cont=0
if p==0:
    cont=cont+1
c=p
while c>0:
    c=c//10
    cont = cont+1
cont2= 0
while q>0:
    if (q%(10**cont))==p:
        cont2 = cont2+1
        break
    q=q//10
if cont2>0:
    print ('S')
else:
    print ('N')