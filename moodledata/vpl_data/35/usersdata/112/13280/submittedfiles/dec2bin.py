# -*- coding: utf-8 -*-
from __future__ import division
a=0

n=input('Digite a quanidade de números:')
j=input('Digite o número:')
l=input('Digite a quanidade de números que contém o subnúmero desejado:')
k=input('Digite o subnúmero que deseja achar:')
cont=0
cont2=0
while j>a:
    if j%(10**cont)==k:
        print('S')
        break
    j=j//10
if cont2>0:
    print('S')
else:
    print('N')