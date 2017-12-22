# -*- coding: utf-8 -*-
import math

a = int(input('Digite valor de a: '))
b = int(input('Digite valor de b: '))

if a>b:
    c = a
else:
    c = b

while True:
    if c%a == 0 and c%b == 0:
        print (c)
        break
    else:
        c = c-1