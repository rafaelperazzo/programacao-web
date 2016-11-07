# -*- coding: utf-8 -*-
from __future__ import division
#COMECE AQUI ABAIXO
n =  input ('Digite o valor de n :')
a = []
for i in range (0,n,1):
        a.append(input ('digite o valor:'))
soma = 1
for i in range (0,n,1):
    soma = soma +(a[i]**2)
print (soma)