# -*- coding: utf-8 -*-
from __future__ import division
a=0

n=input('Digite a quanidade de números:')
j=input('Digite o número:')
l=input('Digite a quanidade de números que contém o subnúmero desejado:')
k=input('Digite o subnúmero que deseja achar:')
cont=0
while a<n:
    if j%(10**l)==j:
        print('É subnúmero')
        break
    a=a//10
if cont>0:
        print('É subnúmero')
else:
    print ('Não é subnúmero')