# -*- coding: utf-8 -*-
from __future__ import division

n=input('Digite a quantidade de valores: ')

l=[]
soma=0
for i in range(0,n,1):
    l.append(input('Digite um valor: '))
    soma=soma+l[i]
media= soma/n
print ('%2.f' %l[0])
print ('%2.f' %l[n-1])
print ('%2.f' %media)
print(l)