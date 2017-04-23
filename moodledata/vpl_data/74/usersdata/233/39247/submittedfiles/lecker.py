# -*- coding: utf-8 -*-
import math
a=int(input('Digite um número qualquer: '))
b=int(input('Digite um número qualquer: '))
c=int(input('Digite um número qualquer: '))
d=int(input('Digite um número qualquer: '))
if a>b and b>c and c>d:
    print('s')
elif d>c and c>b and b>a:
    print('s')
elif b>a and b>c and c>d:
    print('s')
elif c>b and c>d and b>a:
    print('s')
else: 
    print('n')
    