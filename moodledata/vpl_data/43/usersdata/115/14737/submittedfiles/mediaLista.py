# -*- coding: utf-8 -*-
from __future__ import division
n=input('digite os n valores:')
b=[]
for i in range (0,n,1):
    b.append(input('digite um número:'))
s=0
for i in range (0,n,1):
    s=s+b[i]
media=s/n
print('%.2f'%b[0])
print('%.2f'%b[n-1])
print m
print b