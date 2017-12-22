# -*- coding: utf-8 -*-
import math
a = int(input('digite um numero:'))
b= int(input('digite um numero:'))
c = int(input('digite um numero:'))
d= int(input('digite um numero:'))
if a>b:
    print ('S')
elif b>a and b>c:
    print ('S')
elif c>b and c>d:
    print ('S')
elif d>c:
    print ('S')
else :
    print ('N')