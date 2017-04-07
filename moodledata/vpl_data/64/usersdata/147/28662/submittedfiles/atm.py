# -*- coding: utf-8 -*-
from __future__ import division
import math

saque=int(input( 'Digite valor a ser sacado:'))
a=saque//20
print(a)
b=(saque-(a*20))//10
print(b)
c=((saque)-(a*20)-(b*10))//5
print(c)
d=((saque)-(a*20)-(b*10)-(c*5))//2
print(d)
e=((saque)-((a*20)-(b*10)-(c*5)-(d*5)))//1
print(e)


