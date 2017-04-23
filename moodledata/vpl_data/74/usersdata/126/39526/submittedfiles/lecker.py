# -*- coding: utf-8 -*-
import math

a= int(input(' digite o valor 1:'))
b= int(input(' digite o valor 2:'))
c= int(input(' digite o valor 3:'))
d= int(input(' digite o valor 4:'))

if a>b:
    print('S')
elif a<b or b>c:
    print ('S')
elif b<c or c>d:
    print('S')
elif c<d:
    print ('S')
else:
    print ('N')