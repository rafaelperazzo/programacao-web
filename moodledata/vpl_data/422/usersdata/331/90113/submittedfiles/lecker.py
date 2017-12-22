# -*- coding: utf-8 -*-
import math
i = 1
a = int(input('digite um numero:'))
b= int(input('digite um numero:'))
c = int(input('digite um numero:'))
d= int(input('digite um numero:'))
while (i<10):
    if a>b:
    a=1
    elif b>a and b>c:
        print ('S')
    elif c>b and c>d:
        print ('S')
    elif d>c:
        print ('S')
    else :
        print ('N')
print (a)