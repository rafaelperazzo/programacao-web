# -*- coding: utf-8 -*-
from __future__ import division
import math

a = int(input('Digite o valor de a: '))
b = int(input('Digite o valor de b : '))

resto=a%b

while resto != 0:
    a=b
    b=resto
    resto=a%b
    break
print(resto)