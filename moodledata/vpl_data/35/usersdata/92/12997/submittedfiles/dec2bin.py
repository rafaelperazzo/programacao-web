 # -*- coding: utf-8 -*-
from __future__ import division

p= int(input('Digite um valor: '))
q= int(input('Digite um valor: '))

cont=0
while p>1:
    cont= cont+1
    p= p//10
p= p*(10**cont)

x=0
while q>=p:
    if q%(10**cont)==p:
        x=x+1
    q= q//10

if x==0:
    print('N')
else:
    print('S')