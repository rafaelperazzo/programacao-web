# -*- coding: utf-8 -*-
from __future__ import division

n=input("Digite o valor de n: ")
l=[]
for i in range (0,n,1):
    l.append(input("Digite um elemento: "))
somap=0
somai=0
contadorp=0
contadori=0
for i in range (0,n,1):
    if l[i]%2!=0:
        somai=somai+l[i]
        contadori=contadori+1
    else:
        somap=somap+l[i]
        contadorp=contadorp+1
print somai
print somap
print contadori
print contadorp
print l