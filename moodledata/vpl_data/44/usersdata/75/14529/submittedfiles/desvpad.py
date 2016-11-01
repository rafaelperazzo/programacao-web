# -*- coding: utf-8 -*-
from __future__ import division
import math

n=int(input('Digite o valor de n:'))
x=[]

for i in range (0,n,1):
    x.append(input('Digite os elementos da lista:'))

soma=0

for i in range (0,n,1):
    soma=soma+x[i]
    
    media=soma/n
    
d=0
soma=0

for i in range (0,n,1):
    
    soma=soma+((x[i]-media)**2)
    
    d=((1/(n-1)*soma)**0.5)
    
    
print ('%.2f'%x[0])
    
print ('%.2f'%x[n-1])

print ('%.2f'%media)

print ('%.2f'%d)


