# -*- coding: utf-8 -*-
from __future__ import division

n=input('Digite n: ')

b=[]
somap=0
contadorp=0
somai=0
contadori=0
i=0

while i<n:
    b.append(input('Digite um elemento: '))
    
    if (b[i]%2==0):
        somap=somap+b[i]
        contadorp=contadorp+1
    
    else:
        somai=somai+b[i]
        contadori=contadori+1
    
    i=i+1
    
print(somai)
print(somap)
print(contadori)
print(contadorp)
print(b)