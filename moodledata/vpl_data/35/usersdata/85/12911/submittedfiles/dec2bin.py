# -*- coding: utf-8 -*-
from __future__ import division

p= int(input('Digite um número p: '))
q= int(input('Digite um número q: '))

cont=0
c=p
while c>=1:
    c=c//10
    cont=cont+1
cont2=0
while p>0:
    if q%(10**cont)==p:
        cont2=cont2+1
        break
    q=q//10
if cont2>0:
    print('S')
else:
    print('N')