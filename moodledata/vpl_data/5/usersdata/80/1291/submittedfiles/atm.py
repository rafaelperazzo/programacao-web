# -*- coding: utf-8 -*-
from __future__ import division
import math

x=int(input('digite o valor:'))
a=x//20
b=(x%20)//10
c=(b%10)//5
d=(c%5)//2
e=(d%2)
print('o numero de cedulas de 20 é: %.d' %a)
print('o numero de cedulas de 10 é: %.d' %b)
print('o numero de cedulas de 5 é: %.d' %c)
print('o numero de cedulas de 2 é: %.d' %d)
print('o numero de cedulas de 1 é: %.d' %e)

