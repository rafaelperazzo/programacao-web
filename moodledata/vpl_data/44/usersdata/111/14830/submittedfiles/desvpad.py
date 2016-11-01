# -*- coding: utf-8 -*-
from __future__ import division
import math

#comece abaixo

n=input('Digite n: ')

a=[]
b=0
for i in range(0,n,1):
    a.append(input('Digite um valor: '))
    b=b+a[i]
    
media=(b/n)

print ('%.2f' %a[0])
print ('%.2f' %a[n-1])

print ('%.2f' %media)

b=0
for i in range (0,n,1):
    b=b+(a[i] - media)**2
    
    

q=((1)/(n-1))
w=(q*b)**0.5
print ('%.2f' %w)