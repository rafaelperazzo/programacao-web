# -*- coding: utf-8 -*-
import math

a=float(input('Digite o primeiro número:'))
b=float(input('Digite o segundo número:'))
c=float(input('Digite o terceiro número:'))
d=float(input('Digite o quarto número:'))

if a>b:
    if b>=c and c>=d or b<c and c==d:
    print('S')
    else:
        print('N')
elif a<d and b>c:
    if c>=d:
        print('S´)
    else:
        Print('N')
elif b<c and c>d:
    if a<=b:
        print('S')
    else:
        print('N')
elif d>c:
    if a<=b and b<=c or a==b and b>c:
        print('S')
    else:
        print('N')
else:
    print('N')
