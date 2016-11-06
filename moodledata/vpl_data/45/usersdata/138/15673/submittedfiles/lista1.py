# -*- coding: utf-8 -*-
from __future__ import division

n=input('digite a quantidade de números da lista:')
a=[10,11,20,22,30,33,40,44,50,55]
soma=0
soma2=0
for i in range (0,len(a),1):
    if a[i]%2!=0:
        soma=soma+a[i]
    elif a[i]%2==0:
        soma2=soma2+a[i]
print soma
print soma2

