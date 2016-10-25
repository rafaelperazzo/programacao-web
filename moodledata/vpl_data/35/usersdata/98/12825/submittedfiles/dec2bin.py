# -*- coding: utf-8 -*-
from __future__ import division

p=input('Digite o valor de p: ')
q=input('Digite o valor de q: ')
cont=0
cont2=0
c=q
while c>=1:
    c=c//10
    cont=cont+1
while p>0:
    if p%(10**cont)==q:
        cont2=cont2+1
        break
    p=p//10
if cont2>0:
    print('S')
else:
    print('N')