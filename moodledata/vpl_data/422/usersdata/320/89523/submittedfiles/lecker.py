# -*- coding: utf-8 -*-
import math
x = int(input('Digite Numero1: ')
y = int(input('Digite Numero2: ')
z = int(input('Digite Numero3: ')
k = int(input('Digite Numero4: ')
if x==y==z==k:
    print ('N')
elif x>y and z>=y and k<=z:
    print ('S')
elif y>x and y>=z and z>=k:
    print ('S')
elif z>y and z>k and x<=y:
    print ('S')
elif k>z>=y>=x:
    print ('S')
else:
    print ('N')