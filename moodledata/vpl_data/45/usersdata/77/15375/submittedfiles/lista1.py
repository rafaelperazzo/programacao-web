# -*- coding: utf-8 -*-
from __future__ import division

n=input('Digite a quantidade de valores:')

a=[]

for i in range(0,n,1):
    a.apennd(input('Digite os valores da lista:'))
    
soma=0

for i in range(0,n,1):
    if a[i]%2==0:
        soma=soma+a[i]


soma1=0

for i in range(0,n,1):
    if a[i]%2==1:
        soma1=soma1+a[i]
    
print(soma)
print(soma1)
print(a)