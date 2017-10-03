# -*- coding: utf-8 -*-
import math

x = int (input('Digite o valor de x: '))
y = int (input('Digite o valor de y: '))

i = 1
mdc = 0

while (i<=y):
    if (x%i==0) and (y%i==0):
        mdc = i
        print (i)
    i = i + 1
    