# -*- coding: utf-8 -*-
from __future__ import division
import math

x=int(input('digite o valor a ser sacado:'))
a=x//20
b=(x%20)//10
c=((x%20)%10)//5
d=(((x%20)%10)%5)//2
e=(((x%20)%10)%5)%2
print a
print b
print c 
print d
print e