# -*- coding: utf-8 -*-
import math

n = int(input('digite valor de n: '))
a = int(input('digite valor de a: '))
b = int(input('digite valor de b: '))
divisores = []
a1 = 0
b1 = 0

for i in range (0,3,1):
    a1 = a1+a
    b1 = b1+a
divisores.append(a1 and b1)
print (divisores)
