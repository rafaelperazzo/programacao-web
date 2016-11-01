# -*- coding: utf-8 -*-
from __future__ import division
import math

#comece abaixo
n=input('Digite n: ')

l=[]

for i in range(0,n,1):
    l.append(input('Digite um elemento: '))
    
print('%.2f' %l[0])
print('%.2f'%(l[len(l)-1]))

soma=0
for i in range(0,n,1):
    soma=soma+l[i]

media=soma/(len(l))
print('%.2f' %media)

soma=0
for i in range(0,n,1):
    soma=soma+((l[i]-media)**2)

desvio=(soma/(n-1))**(0.5)

print('%.2f'%desvio)
    

    
    
    
    
    
    
    
    
    
    
    
    
    