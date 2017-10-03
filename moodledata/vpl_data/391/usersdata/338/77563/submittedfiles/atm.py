# -*- coding: utf-8 -*-
from __future__ import division
import math

#COMECE SEU CODIGO AQUI
x = (int(input('digite o valor a ser sacado: ')))
n20 = x//20
n10 = (x - ((n20)*20))//10
n5 = ((x - (n20)*20 - (n10)*10)//5)
n2 = ((x - (n20)*20 - (n10)*10 - (n5)*5)//2)
n1 = ((x - (n20)*20 - (n10)*10 - (n5)*5 - (n2)*2)//1)


print(n20 notas de 20)
print(n10 notas de 10)
print(n5 notas de 5)
print(n2 notas de 2)
print(n1 notas de 1)
