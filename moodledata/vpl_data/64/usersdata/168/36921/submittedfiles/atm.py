# -*- coding: utf-8 -*-
from __future__ import division
import math
v=int(input('Digite o valor que será sacado: '))
n1=v//20
n2=(v%20)//10
n3=((v%20)%10)//5
n4=(((v%20)%10)%5)//2
n5=((((v%20)%10)%5)%2)//1
print('%.1d'%n1)
print('%.1d'%n2)
print('%.1d'%n3)
print('%.1d'%n4)
print('%.1d'%n5)