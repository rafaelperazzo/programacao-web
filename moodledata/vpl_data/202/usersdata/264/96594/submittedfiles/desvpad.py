# -*- coding: utf-8 -*-
import math

#comece abaixo
n= int(input('Digite o valor dos n elementos:'))
a= []
for i in range(0,n,1):
    valor= int(input('Digite o valor de cada um dos termos da lista:'))
    a.append (valor)

print ('%.2f' %a[0])