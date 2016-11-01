 # -*- coding: utf-8 -*-
from __future__ import division

p= int(input('Digite um valor: '))
q= int(input('Digite um valor: '))

h=p
cont=0
while h>1:
    cont= cont+1
    h= h//10


x=0
while q>=1:
    if q%(10**cont)==p:
        x=x+1
        break
    q= q//10

if x>0:
    print('S')
else:
    print('N')