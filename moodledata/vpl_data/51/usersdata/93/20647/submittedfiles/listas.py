# -*- coding: utf-8 -*-
from __future__ import division
n=5
a=[]
for i in range(0,n,1):
    a.append(input('elemento da lista: '))
maior = 0
for i in range(1,n,1):
    if ((a[i]-a[i-1])**2)**0.5>maior:
        maior=((a[i]-a[i-1])**2)**0.5
print maior
