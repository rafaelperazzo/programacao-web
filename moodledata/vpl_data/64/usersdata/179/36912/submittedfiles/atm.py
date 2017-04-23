# -*- coding: utf-8 -*-
from __future__ import division
import math
v=int(input('digite o valor:'))
s1=v//20
s2=(v%20)//10
s3=((v%20)%10)//5
s4=(((v%20)%10)%5)//2
s5=((((v%20)%10)%5)%2)//1
print('%d'%s1)
print('%d'%s2)
print('%d'%s3)
print('%d'%s4)
print('%d'%s5)
