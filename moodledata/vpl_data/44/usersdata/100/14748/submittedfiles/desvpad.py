# -*- coding: utf-8 -*-
from __future__ import division
import math
#comece abaixo#
l = []
n =  input ('Digite n:')
#Media#
for i in range(0,n,1):
    l.append(input ('Digite os valores:'))
soma = 0
for k in range (0,n,1):
  soma = soma+l[k] 
  c = soma /n
#Fim da Media ###########
soma2 = 0
for b in range (0,n,1):
    x = (l[b]-c)**2
    soma2 = soma2+x
z = (soma2/(n-1))**(1/2)
print ('%.2f' %l[0])
print ('%.2f'%(l[n-1]))
print ('%.2f'%c)
print ('%.2f'%z)

