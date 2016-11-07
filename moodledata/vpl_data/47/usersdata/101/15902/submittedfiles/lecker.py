# -*- coding: utf-8 -*-
from __future__ import division

n = input('Digite a quantidade de elesmentos: ')
a = []
b = []

for i in range (0,n,1):
    a.append(input('Digite o elemento da lista: '))
    if a[0]<a[i]:
        print ('S')
    else:
        print ('N')
    
for i in range (0,n,1):
    b.append(input('Digite o elemento da lista: '))
    if b[0]<b[i]:
        print ('S')
    else:
        print ('N')