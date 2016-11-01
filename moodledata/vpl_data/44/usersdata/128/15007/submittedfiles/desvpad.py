# -*- coding: utf-8 -*-
from __future__ import division
import math

#comece abaixo

n=input('Digite a quantidade de termos: ')

x=[]
soma=0
somatorio=0

for i in range (0,n,1):
    x.append(input('Digite um termo: '))
    soma=soma+x[i]
    media=soma/n
    somatorio=somatorio+((x[i]-media)**2)

s=(((1/(n-1))*somatorio)**0.5)
print ('%.2f' %x[0])
print ('%.2f' %x[n-1])
print ('%.2f' %media)
print ('%.2f' %s)