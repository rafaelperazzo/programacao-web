# -*- coding: utf-8 -*-
from __future__ import division

n = input ('Digite a quantidade de elementos da lista:')
a = []
Soma = 0
for i in range (0,n,1):
    a.append (input ('Digite um número:'))
    Soma = Soma + a[i]
    Md = Soma / len (a)
print ('%.2f' %a[0])
print ('%.2f' %a[len(a)-1])
print ('%.2f' %Md)
print (a)