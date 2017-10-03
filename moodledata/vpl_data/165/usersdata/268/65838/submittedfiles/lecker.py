# -*- coding: utf-8 -*-
import math

a=int(input(' Digite o valor a: '))
b=int(input(' Digite o valor b: '))
c=int(input(' Digite o valor c: '))
d=int(input(' Digite o valor d: '))

if (a>b) and ( b>=c) and (c>=d):
    print('S')
elif (d>c) and (c<=b) and (b<=a):
    print ('S')
elif (a<b) and (b>c) and (c>=d):
    print('S')
elif (c>d) and (c>b) and (b>=a):
    print('S')
else:
    print('N')