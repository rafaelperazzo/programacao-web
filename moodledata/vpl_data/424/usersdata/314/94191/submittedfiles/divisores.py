# -*- coding: utf-8 -*-
import math

n = int(input('Digite o valor de n: '))
a = int(input('Digite o valor de a: '))
b = int(input('Digite o valor de b: '))

if (a < b):
    i = a
else :
    i = b

while (n > 0) :
    if (i%a == 0) or (i%b == 0):
        print(i)
        n -= 1
    i += 1
