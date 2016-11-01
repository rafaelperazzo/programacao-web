# -*- coding: utf-8 -*-
from __future__ import division
import math

n = input ('insira o valor de n:')

a=[]

for i in range (0,n,1):
    a.append(input('insira um valor:'))
    
cont=0

for j in range (0,n,1):
    cont=cont+a[j]
     
media=cont/n

cont2=0
for k in range (0,n,1):
    m=(a[k]-media)**2
    cont2=cont2+m
    
s=((1/(n-1))*cont2)**(1/2)

print ('%.2f' %a[0])
print ('%.2f' %a[n-1])
print ('%.2f' %media)
print ('%.2f' %s)
