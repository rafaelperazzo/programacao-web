# -*- coding: utf-8 -*-
from __future__ import division
import math

v=int(input('digite o valor que deseja sacar:'))
k1=v//20
k2=(v%20)//10
k3=((v%20)%10)//5
k4=(((v%20)%10)%5//2
k5=((((v%20)%10)%5)%2)//1
print('notas de 20 reais:%d'%k1)
print('notas de 10 reais:%d'%k2)
print('notas de 5 reais:%d'%k3)
print('notas de 2 reais:%d'%k4)
print('notas de 1 reais:%d'%k5)