# -*- coding: utf-8 -*-
from __future__ import division
import math

valor=input('digite a quantia que você deseja sacar')
a=(valor/20)
b=((valor%20)/10)
c=(((valor%20)%10)/5)
d=(((((valor%20)%10)%5)/2))
e=(valor)-((a*20)+(b*10)+(c*5)+(d*2))
print('%i'%a)
print('%i'%b)
print('%i'%c)
print('%i'%d)
print('%i'%e)