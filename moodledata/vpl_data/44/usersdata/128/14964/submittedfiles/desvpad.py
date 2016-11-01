# -*- coding: utf-8 -*-
from __future__ import division
import math

#comece abaixo

n=input('Digite a quantidade de termos: ')

x=[]
soma=0

for i in range (0,n,1):
    x.append(input('Digite um termo: '))
    soma=soma+x[i]
    media=soma/n
    dp=((1/(n-1)*((x[i]-media)**2))**0.5)
    
print dp