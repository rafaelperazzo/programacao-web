# -*- coding: utf-8 -*-
from __future__ import division
import math

v=int(input('digite o valor'))
s1=v//20
s2=(v%20)//10
s3=((v%20)%10)//5
s4=(((v%20)%10)%5)//2
s5=((((v%20)%10)%5)%2)//1
print('sedulas de 20 reais:%d'%s1)
print('sedulas de 10 reais:%d'%s2)
print('sedulas de 5 reais:%d'%s3)
print('sedulas de 2 reais:%d'%s4)
print('sedulas de 1 reais:%d'%s5)
