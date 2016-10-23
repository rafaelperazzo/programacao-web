# -*- coding: utf-8 -*-
from __future__ import division
q=int(input(('Digite um número:'))
p=int(input(('Digite um número:'))
cont=0
a=p
while a>=1:
    a=a//10
    cont=cont+1
cont2=0
while p>0:
    if p%(10**contador)==q:
        cont2=cont2+1
        break
    p=p//10
if cont2>0:
    print ('S')
else:
    print ('N')