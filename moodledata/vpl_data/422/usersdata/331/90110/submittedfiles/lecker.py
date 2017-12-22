# -*- coding: utf-8 -*-
import math
i = 1
a = int(input('digite um numero:'))
b= int(input('digite um numero:'))
c = int(input('digite um numero:'))
d= int(input('digite um numero:'))
while (i<10):
    if a>b:
        print ('S1')
        break
    elif b>a and b>c:
        print ('S2')
        break
    elif c>b and c>d:
        print ('S3')
        break
    elif d>c:
        print ('S4')
        break
    else :
        print ('N')