# -*- coding: utf-8 -*-
from __future__ import division

n= input('Digite o valor de n: ')
a=[]

for i in range(0,n,1):
    a.append(input('Digite o valor de n: '))
si=0
for i in range(0,n,1):
    if a[i]%2!=0:
        si=si+a[i]
sp=0
for i in range(0,n,1):
    if a[i]%2==0:
        sp=sp+a[i]
