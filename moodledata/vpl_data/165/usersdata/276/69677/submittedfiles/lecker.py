# -*- coding: utf-8 -*-
import math

a = float(input('Digite o valor de a: '))
b = float(input('Digite o valor de b: '))
c = float(input('Digite o valor de c: '))
d = float(input('Digite o valor de d: '))

if (a<b) and (b<c) and (c<d):
    print ('S')
elif (a<b) and (b>c) and (c>d):
    print ('S')
elif (a<b) and (b<c) and (c>d):
    print ('S')
elif (a>b) and (b>c) and (c>d):
    print ('S')
elif (a>b) and (b==c) and (b==d):
    print('S')
elif (a>b) and (a==c) and (a==d):
    print ('S')
elif (b>a) and (a==c) and (c==d):
    print ('S')
elif (b>a) and (b==c) and (b==d):
    print ('S')
elif (c>a) and (a==b) and (b==d):
    print ('S')
elif (c>a) and (c==b) and (c==d):
    print ('S')
elif (d>a) and (a==b) and (b==c):
    print ('S')
elif (d>a) and (d==b) and (d==c):
    print ('S')
else:
    print ('N')