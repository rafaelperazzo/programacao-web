# -*- coding: utf-8 -*-
import math

num1=float(input('Digite o número 1: '))
num2=float(input('Digite o número 2: '))
num3=float(input('Digite o número 3: '))
num4=float(input('Digite o número 4: '))

if a<b and b<c and c<d:
    print('S')
elif a<b and b>c and c>d:
    print('S')
elif a<b and b<c and c>d:
    print('S')
elif a>b and b>c and c>d:
    print('S')
elif a<b and b==c and b==d:
    print('S')
elif a<b and a==c and a==d:
    print('S')
elif a<b and a==c and c==d:
    print('S')
elif a<b and b==c and b==d:
    print('S')
elif c>a and a==b and b==d:
    print('S')
elif c>a and c==b and c==d:
    print('S')
elif d>a and a==b and b==c:
    print('S')
else:
    print('N')