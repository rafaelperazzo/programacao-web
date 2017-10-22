# -*- coding: utf-8 -*-
import math
a = int(input('Digite o primeiro número: '))
b = int(input('Digite o segundo número: '))
c = int(input('Digite o terceiro número: '))
d = int(input('Digite o quarto número: '))
if a > b and b < c and c > d:
    print('S')
elif a < b and b > c and c > d:
    print('S')
elif c > b and d < c and a < b:
    print('S')
elif d > c and c > b and b > a:
    print('S')


elif a > b and b == c and c == d:
    print('S')
elif a > b and b < c and c == d:
    print('S')
elif a < b and b > c and c == d:
    print('S')
elif c > b and d < c and a == b:
    print('S')
elif d > c and b == c and b == a:
    print('S')
elif d > c and b > c and a == b:
    print('S')
else:
    print('N')