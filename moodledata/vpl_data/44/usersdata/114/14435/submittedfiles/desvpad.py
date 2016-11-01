# -*- coding: utf-8 -*-
from __future__ import division
import math

#comece abaixo

n=input('digite o valor de n: ')
lista=[]

for i in range (0,n,1):
    lista.append(input('digite um valor: '))
    
soma=lista[0]
for i in range (1,n,1):
    soma=soma + lista[i] 
media=soma/n

soma=0
for j in range (0,n,1):
    soma=soma+(1[j]-ma)**2
s=((1/(n-1))*soma)**0.5    



print ('%.2f' %lista[0])
print ('%.2f' %lista[n-1])
print ('%.2f' %media)
print lista