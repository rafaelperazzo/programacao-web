# -*- coding: utf-8 -*-
from __future__ import division
a=input('Digite o número:')
b=input('Digite a quantidade algarismos:')
c=input('Digite o subnúmero:')
d=input('Digite a quantidade de números:')
cont=0
while a>0:
    if a%(10**d)==c:
        print('S')
        break
    a=a//10
if cont>0:
    print('S')
if cont==0:
    print('N')
    