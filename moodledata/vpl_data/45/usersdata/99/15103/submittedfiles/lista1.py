# -*- coding: utf-8 -*-
from __future__ import division

n=int(input('Digite um valor para n:'))
L=[]

for i in range (0,n,1):
    L.append(input('Digite valores para L:'))
    
contadori=0
somai=0
contadorp=0
somap=0
for i in range (0,n,1):
    if L[i]%2!=0:
        contadori=contadori+1
        somai=somai+L[i]
        
    else:
        contadorp=contadorp+1
        somap=somap+1
        
print somai
print somap
print contadori
print contadorp
print L
        
        
