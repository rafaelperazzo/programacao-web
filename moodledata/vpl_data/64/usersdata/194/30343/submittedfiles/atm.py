# -*- coding: utf-8 -*-
from __future__ import division
import math

v=int(input('Digite o valor que deseja sacar:'))
n1=v//20
n2=(v%20)//10
n3=((v%20)%10)//5
n4=(((v%20)%10)%5)//2
n5=((((v%20)%10)%5)%2)//1
print('cédulas de 20 reais:%d'%n1)
print('cédulas de 10 reais:%d'%n2)
print('cédulas de 5 reais:%d'%n3)
print('cédulas de 2 reais:%d'%n4)
print('cédulas de 1 reais:%d'%n5)