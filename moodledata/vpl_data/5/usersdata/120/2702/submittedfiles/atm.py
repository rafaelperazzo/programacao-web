# -*- coding: utf-8 -*-
from __future__ import division
import math

#ENTRADA
v=int(input('informe o valor a ser sacado:')
#PROCESSAMENTO
nota20=(v//20)
a=(v-(nota20*20))
nota10=(a//10)
b=(a-(nota10*10))
nota5=(b//5)
c=(b-(nota5*5))
nota2=(c//2)
d=(c-(nota2*2))
nota1=d
#SAIDA
print('%d'%nota20)
print('%d'%nota10)
print('%d'%nota5)
print('%d'%nota2)
print('%d'%nota1)



