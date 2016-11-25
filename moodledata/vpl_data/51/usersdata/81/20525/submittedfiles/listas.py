# -*- coding: utf-8 -*-
from __future__ import division
import math

def degrau(a):
    maior=0
    for i in range(0,len(a)-1,1):
        degrau=math.fabs(a[i]-a[i+1])
        maior=degrau
    return maior
    
t=[]
n=input('Digite a quantidade de elementos de t')
for i in range (0,n-1,1):
    t.append(input('Digite o elemento de t:'))
    
valor= degrau(t)
print ('%.d' %valor)