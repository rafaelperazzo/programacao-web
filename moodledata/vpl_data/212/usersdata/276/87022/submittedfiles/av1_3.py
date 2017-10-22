# -*- coding: utf-8 -*-
import math

a = int(input('Digite a: '))
b = int(input('Digite b: '))
c = int(input('Digite c: '))

i = 1

while (i<c):
    if (i%a ==0) and (i%b==0) and (i%c==0):
        print (i)
    else:
        i = i + 1
