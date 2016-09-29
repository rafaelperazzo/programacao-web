# -*- coding: utf-8 -*-
from __future__ import division
import math
#ENTRADA
valor = int(input('Digite o valor:'))

#PROCESSAMENTO
v1 = valor//20 
v2 = (valor%20)//10
v3 = ((valor%20)%10)//5
v4 = (((valor%20)%10)%5)//2
v5 = ((((valor%20)%10)%5)%2)//1

#SAIDA
print ('%d' %v1)
print ('%d' %v2)
print ('%d' %v2)
print ('%d' %v3)
print ('%d' %v4)
