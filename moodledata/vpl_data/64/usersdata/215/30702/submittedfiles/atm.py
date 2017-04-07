# -*- coding: utf-8 -*-
from __future__ import division
import math
v=int(input('digite O VALOR QUE DESEJA SACAR:'))
n1=v//20
n2=(v%20)//10
n3((v%20)%10)//5
n4(((v%20)%10)%5)//2
n5((((v%20)%10)%5)%2)//1
print('notas de 20reais:%d'%n1)
print('notas de 10reais:%d'%n2)
print('notas de 5reais:%d'%n3)
print('notas de 2reais:%d'%n4)
print('notas de 1reais:%d'%n5)
