# -*- coding: utf-8 -*-
import math

a= int(input('Digite o valor de a: '))
b= int(input('Digite o valor de b: '))
c= int(input('Digite o valor de c: '))
d= int(input('Digite o valor de d: '))

if (a>b) and (a>c) and (a>d):
    print('S')

elif (b>a) and (b>c) and (b>d):
    print('S')

elif (c>a) and (c>b) and (c>d):
    print('S')

elif (d>a) and (d>b) and (d>c):
    print('S')

else:
    print('N')


