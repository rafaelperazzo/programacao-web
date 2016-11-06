# -*- coding: utf-8 -*-
from __future__ import division
#ENTRADA
n=input('digite o valor de n:')
a=[]

#SAIDA
for i in range (0,n,1):
    a.append(input('digite o valor do proximo termo:'))
    if a[i]%2!=0:
        print (a[i])
    soma=soma    
