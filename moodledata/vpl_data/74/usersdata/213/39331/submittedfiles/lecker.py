# -*- coding: utf-8 -*-
import math

a=int(input('Informe o 1° número: '))
b=int(input('Informe o 2° número: '))
c=int(input('Informe o 3° número: '))
d=int(input('Informe o 4° número: '))

if a>b>c>d:
    print('S')
elif a>b>d>c:
    print('S')
elif a>c>b>d:
    print('S')
elif a>c>d>b:
    print('S')
elif a>d>c>b:
    print('S')
elif a>d>b>c:
    print('S')
elif b>a>c>d:
    print('S')
elif b>s>d>c:
    print('S')
elif b>c>a>d:
    print('S')
elif b>c>d>a:
    print('S')
elif b>d>c>a:
    print('S')
elif b>d>a>c:
    print('S')
elif c>b>a>d:
    print('S')
elif c>b>d>a:
    print('S')
elif c>a>b>d:
    print('S')
elif c>a>d>b:
    print('S')
elif c>d>a>b:
    print('S')
elif c>d>b>a:
    print('S')
elif d>b>a>c:
    print('S')
elif d>b>c>a:
    print('S')
elif d>a>b>c:
    print('S')
elif d>a>c>b:
    print('S')
elif d>c>a>b:
    print('S')
elif d>c>b>a:
    print('S')
else:
    print('N')