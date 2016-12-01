# -*- coding: utf-8 -*-
from __future__ import division
import math

maior=0
def degraumaior(a):
    for i in range (0,len(a)-1,1):
        degrau=math.fabs(a[i]-a[i-1])
        maior=degrau
    return degrau
    
n=input('Digite o valor de n: ')

a=[]
for i in range (0,n,1):
    a.append(input('Digite um elemento de a: '))
    
print degraumaior(a)
