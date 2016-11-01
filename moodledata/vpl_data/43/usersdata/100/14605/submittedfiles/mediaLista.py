# -*- coding: utf-8 -*-
from __future__ import division
l = []
n =  input ('Digite n:')
for i in range(0,n,1):
    l.append(input ('Digite os valores:'))
    """ Agora, mais uma repetição para definirmos a soma dos valores"""
soma = 0
for k in range (0,n,1):
  soma = soma+l[k] 
  c = soma /n
print l[0]
print l[n]
print c
print [l]
