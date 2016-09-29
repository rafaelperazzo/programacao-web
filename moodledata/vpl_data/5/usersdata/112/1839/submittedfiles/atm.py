# -*- coding: utf-8 -*-
from __future__ import division
import math

valor=input('digite a quantia que você deseja sacar')
v= (valor)-(valor%1)
a=(v/20)
b=((v%20)/10)
c=(((v%20)%10)/5)
d=(((((v%20)%10)%5)/2))
e=(v)-((a*20)+(b*10)+(c*5)+(d*2))
print('%i'%a)
print('%i'%b)
print('%i'%c)
print('%i'%d)
print('%i'%e)