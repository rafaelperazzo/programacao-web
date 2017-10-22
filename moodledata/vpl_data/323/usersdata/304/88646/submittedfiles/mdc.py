# -*- coding: utf-8 -*-
import math
a = int(input('x: '))
b = int(input('y: '))
while b !=0:
    resto = a%b
    a = b
    b = resto
mdc = a
print(mdc)
