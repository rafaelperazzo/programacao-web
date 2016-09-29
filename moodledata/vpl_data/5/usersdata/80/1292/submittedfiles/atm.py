# -*- coding: utf-8 -*-
from __future__ import division
import math

x=int(input('digite o valor:'))
a=x//20
b=(x-(20*a))//10
c=(x-((20*a)+(10*b)))//5
d=(x-((20*a)+(10*b)+(5*c)))//2
e=(x-((20*a)+(10*b)+(5*c)+(2*d)))//1
print('o numero de cedulas de 20 é: %.d' %a)
print('o numero de cedulas de 10 é: %.d' %b)
print('o numero de cedulas de 5 é: %.d' %c)
print('o numero de cedulas de 2 é: %.d' %d)
print('o numero de cedulas de 1 é: %.d' %e)

