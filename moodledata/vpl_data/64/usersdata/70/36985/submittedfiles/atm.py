# -*- coding: utf-8 -*-
from __future__ import division
import math
v=int(input('Didgite o valor: '))
n1=v//20
n2=(v%20)//10
n3=((v%20)%10)//5
n4=(((v%20)%10)%5)//1
n5=((((v%20)%10)%5)%2)//1
print('Notas de 20:%d'%n1)
print('Notas de 10:%d'%n2)
print('Notas de 5:%d'%n3)
print('Notas de 2:%d'%n4)
print('Notas de 1:%d'%n5)


