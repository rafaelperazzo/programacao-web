# -*- coding: utf-8 -*-
from __future__ import division

n=input('Digite a quantidade de números da sequencia:')
a=[]

for i in range (0,n,1):
    a.append('Digite um número da lista')
    if a[i-1]>a[i]:
        cont==a[i]