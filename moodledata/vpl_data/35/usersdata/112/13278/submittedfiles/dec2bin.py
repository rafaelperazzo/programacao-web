# -*- coding: utf-8 -*-
from __future__ import division
a=0
hj=0
n=input('Digite a quanidade de números:')
j=input('Digite o número:')
l=input('Digite a quanidade de números que contém o subnúmero desejado:')
k=input('Digite o subnúmero que deseja achar:')

while a<n:
    kq=j//(10**l)
    if j%(10**l)==j:
        print('É subnúmero')
        break
    a=a//10
if hj>0:
        print('É subnúmero')
else:
    print ('Não é subnúmero')