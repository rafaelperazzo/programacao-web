# -*- coding: utf-8 -*-
from __future__ import division

p= int(input('Digite o valor de p: '))
q= int(input('Digite o valor de q: '))
cont=0
c=q
while c>0:
    c=c//10
    cont=cont+1
cont2=0
while p>0:
    if p%(10**cont)==q:
        