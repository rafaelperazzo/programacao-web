# -*- coding: utf-8 -*-
from __future__ import division
import math

x=int(input('digite o valor:'))
a=x//20
b=(x-(20*a))//10
c=(x-((20*a)+(10*b)))//5
d=(x-((20*a)+(10*b)+(5*c)))//2
e=(x-((20*a)+(10*b)+(5*c)+(2*d)))//1
print a
print b
print c
print d
print e

