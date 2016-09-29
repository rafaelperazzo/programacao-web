# -*- coding: utf-8 -*-
from __future__ import division

#entrada
p = input ('Digite um valor para p:')
i = input ('Digite um valor para i:')
n = input ('Digite um valor para n:')

#processamento:
V = p* ((((1+i)**n)-1)/i)

#saída
print ('%.1f' %V)