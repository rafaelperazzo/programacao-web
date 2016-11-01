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
    dp=((x[i]-media)**2)
    
s=(((1/(n-1))*dp)**0.5)
print s