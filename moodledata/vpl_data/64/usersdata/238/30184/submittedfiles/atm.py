# -*- coding: utf-8 -*-
from __future__ import division
import math

v=int(input('digite o valor do saque:'))
n1=v//20
n2=(v%20)//10
n3=((v%20)%10)//5
n4=(((v%20)%10)%5)//2
n5=((((v%20)%10)%5)%2)//1
print('%d' %n1)
print('%d' %n2)
print('%d' %n3)
print('%d' %n4)
print('%d' %n5)
