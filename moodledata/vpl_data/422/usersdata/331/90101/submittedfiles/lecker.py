# -*- coding: utf-8 -*-
import math
a = int(input('digite um numero:'))
b= int(input('digite um numero:'))
c = int(input('digite um numero:'))
d= int(input('digite um numero:'))
if a>b or b>a and b>c or c>b and c>d or d>c:
    print ('S')
else :
    print ('N')