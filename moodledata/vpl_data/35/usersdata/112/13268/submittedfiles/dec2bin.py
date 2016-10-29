# -*- coding: utf-8 -*-
from __future__ import division

a=input('Digite o número:')
b=input('Digite o subnúmero:')

cont=0
c=b
while c>=1:
    c=c//10
    cont=cont+1
cont2=0
while (a>0):
    if a%(10**cont)==b:
        print('S')
        break
    a=a//10
if cont2>0:
    print('S')
elif cont2==0:
    print('N')