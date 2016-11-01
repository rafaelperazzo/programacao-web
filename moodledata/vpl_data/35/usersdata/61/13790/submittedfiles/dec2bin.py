# -*- coding: utf-8 -*-
from __future__ import division
q=int(input('Digite um n: '))
p=int(input('Digite um n: '))
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
    print ('S')
else:
    print ('N')
