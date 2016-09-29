# -*- coding: utf-8 -*-
from __future__ import division
import math

#ENTRADA
valor=int(input('informe o valor a ser sacado:')
#PROCESSAMENTO
nota20=(valor//20)
a=(valor-(nota20*20))
nota10=(a//10)
b=(a-(nota10*10))
nota5=(b//5)
c=(b-(nota5*5))
nota2=(c//2)
d=(c-(nota2*2))
nota1=d
#SAIDA
print(nota20)
print(nota10)
print(nota5)
print(nota2)
print(nota1)



