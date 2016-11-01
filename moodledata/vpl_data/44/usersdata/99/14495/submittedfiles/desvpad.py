# -*- coding: utf-8 -*-
from __future__ import division
import math

#comece abaixo
n=int(input('Digite o valor de n:'))
X=[]

for i in range (0,n,1):
    X.append(input('Digite valores para X:')
    
print ('%.2f'%X[0])
print ('%.2f'%X[n-1])

soma=0
for i in range (0,n,1):
    soma=soma+X[i]
media=soma/n
print('%.2f'%media)

d=0
soma=0
for i in range (0,n,1):
    soma=soma+((Xi-media)**2)
d=((1/(n-1))*soma)**0.5
print('%.2f'%d)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
