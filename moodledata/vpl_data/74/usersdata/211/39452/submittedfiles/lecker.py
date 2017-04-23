# -*- coding: utf-8 -*-
import math
c=float(input('escreva o valor de c:'))
d=float(input('escreva o valor de d:'))
e=float(input('escreva o valor de e:'))
f=float(input('escreva o valor de f:'))
if d>c and d>e and e<f:
    print('N')
elif e>f and e>d and c>d:
    print('N')
elif d>c and d>e or e>d and e>f:
    print('S')
elif c>d and e<f:
    print('N')
elif c>d or f>e:
    print('S')
else:
    print('N')
