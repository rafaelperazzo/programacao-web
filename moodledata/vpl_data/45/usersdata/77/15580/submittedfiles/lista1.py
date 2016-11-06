# -*- coding: utf-8 -*-
from __future__ import division

n=input('Digite a quantidade de valores:')

a=[]

for i in range(0,n,1):
    a.append(input('Digite os valores da lista:'))
    
somap=0
contadorp=0

for i in range(0,n,1):
    if a[i]%2==0:
        somap=somap+a[i]
        contadorp=contadorp+1
somai=0
contadori=0
for i in range(0,n,1):
    if a[i]%2==1:
        somai=somai+a[i]
        contadori=contadori+1
print(somai)
print(somap)
print(contadori)
print(contadorp)
print(a)