# -*- coding: utf-8 -*-
from __future__ import division
import math

#comece abaixo
n = input ('Digite a quantidade de elementos da lista:')
a = []
Soma = 0
Soma2 = 0
for i in range (0,n,1):
    a.append (input ('Digite um número:'))
    Soma = Soma + a[i]
Md = Soma / len (a)
for y in range (0,n,1):
    Soma2 = Soma2+((a[y]-Md)**2)
S = (Soma2/(len(a)-1))**0.5
print ('%.2f' %a[0])
print ('%.2f' %a[len(a)-1])
print ('%.2f' %Md)
print ('%.2f' %S)