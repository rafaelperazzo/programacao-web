# -*- coding: utf-8 -*-
from __future__ import division
import math

x = int(input ('insira o valor a ser sacado:'))

m1 = x-(x%100)
c1 = m1/20

m2 = (x%100)-((x%100)%10)
c21 = math.floor(m2/20)
c22 = math.floor((m2-c21)/10)

m3 = (x%100)%10
c31 = math.floor(m3/5) 
c32 = math.floor((m3-c31)/2)
c33 = m3-c31-c32

A = c1+c21
B = c22
C = c31
D = c32
E = c33

print A
print B
print C
print D
print E

