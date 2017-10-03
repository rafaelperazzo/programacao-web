# -*- coding: utf-8 -*-
from __future__ import division
import math

#COMECE SEU CODIGO AQUI
x = int(input('Digite o valor a ser sacado: '))
a = x//20
b = (x-a)//10
c = (x-a-b)//5
d = (x-a-b-c)//2
e = (x-a-b-c-d)//1
print(a)
print(b)
print(c)
print(d)
print(e)