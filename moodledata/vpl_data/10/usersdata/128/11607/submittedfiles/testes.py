# -*- coding: utf-8 -*-
from __future__ import division

#COMECE AQUI ABAIXO

n=input('Digite n: ')
soma=0
for i in range (0,n+1,1):
    pi=(-1**i)/(2*i+1)
    soma=soma+pi
print (soma*4)