# -*- coding: utf-8 -*-
import math

#comece abaixo
n=int(input('digite ovalor do número de elementos da lista:'))
a=[]
for i in range(0,n,1):
    v=float(('digite um valor:'))
    a.append(v)
soma=0
for cont in range(0,n,1):
    soma=soma+a[cont]
m=soma/n
