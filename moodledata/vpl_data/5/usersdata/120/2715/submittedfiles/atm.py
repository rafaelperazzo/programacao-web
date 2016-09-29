# -*- coding: utf-8 -*-
from __future__ import division
import math

#ENTRADA
v=int(input('informe o valor a ser sacado:'))
#PROCESSAMENTO
n20=(v//20)
a=(v-(n20*20))
n10=(a//10)
b=(a-(n10*10))
n5=(b//5)
c=(b-(n5*5))
n2=(c//2)
d=(c-(n2*2))
n1=d
#SAIDA
print('%d'%n20)
print('%d'%n10)
print('%d'%n5)
print('%d'%n2)
print('%d'%n1)



