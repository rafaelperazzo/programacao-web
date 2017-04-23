# -*- coding: utf-8 -*-
import math
a=int(input('Digite o valor de a:'))
b=int(input('Digite o valor de b:'))
c=int(input('Digite o valor de c:'))
d=int(input('Digite o valor de d:'))
if a<b and a<c and a<d and b<c and b<d and c<d:
    print('S')
elif a<b and a<c and a<d and b<c and b<d and c>d:
    print('S')
elif a<b and a<c and a<d and b>c and c<d and b>d:
    print('S')
elif a>b and a>c and a>d and b<c and b<d and c<d:
    print('S')
else:
    print('N')