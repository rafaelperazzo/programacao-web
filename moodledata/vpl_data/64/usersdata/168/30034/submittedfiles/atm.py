# -*- coding: utf-8 -*-
from __future__ import division
import math
v=int(input('Digite o valor que será sacado:'))
n1=v//20
n2=(v%20)//10
n3=((v%20)%10)//5
n4=(((v%20)%10)%5)//2
n5=((((v%20)%10)%5)%2)//1
print('notas de 20: %d'%n1)
print('notas de 10: %d'%n2)
print('notas de 5: %d'%n3)
print('notas de 2: %d'%n4)
print('notas de 1: %d'%n5)
print('volte sempre')