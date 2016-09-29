# -*- coding: utf-8 -*-
from __future__ import division
import math

#ENTRADA:
v = (int(input('Digite o valor que será sacado:'))

#PROCESSAMENTO:
n20=(v//20)
n10=((v//20)//10)
n5=(((v//20)//10)//5)
n2=((((v//20)//10)//5)//2)
n1=(((((v//20)//10)//5)//2)//1)

#SAIDA:
print ('%.1f'%n20)
print ('%.1f'%n10)
print ('%.1f'%n5)
print ('%.1f'%n2)
print ('%.1f'%n1)