# -*- coding: utf-8 -*-
from __future__ import division
import math

#COMECE SEU CODIGO AQUI
y = int(input("Digite o valor a ser sacado:"))
a = y//20
b = (y-(20*a))//10
c = (y-((20*a)+(10*b)))//5
d = (y-((20*a)+(10*b)+(5*c)))//2
e = (y-((20*a)+(10*b)+(5*c)+(2*d)))//1
print(a)
print(b)
print(c)
print(d)
print(e)
