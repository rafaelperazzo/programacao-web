# -*- coding: utf-8 -*-
from __future__ import division
import math

#ENTRADA:
v=(int(input('Digite o valor que será sacado:'))

#PROCESSAMENTO:
n1=(v//20)
n2=((v//20)//10)
n3=(((v//20)//10)//5)
n4=((((v//20)//10)//5)//2)
n5=(((((v//20)//10)//5)//2)//1)

#SAIDA:
print ('%.1f'%n1)
print ('%.1f'%n2)
print ('%.1f'%n3)
print ('%.1f'%n4)
print ('%.1f'%n5)