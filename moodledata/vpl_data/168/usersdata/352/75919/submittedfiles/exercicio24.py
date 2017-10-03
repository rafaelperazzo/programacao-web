# -*- coding: utf-8 -*-
import math

a=int(input('Digite o valor de a:'))
b=int(input('Digite o valor de b:'))

while b!=0:
    resto=a%b
    a=b
    b=resto
print(a)