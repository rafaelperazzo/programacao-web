# -*- coding: utf-8 -*-
import math
a=int(input('Digite o valor do número a:'))
b=int(input('Digite o valor do número b:'))
c=int(input('Digite o valor do número c:'))
d=int(input('Digite o valor do número d:'))
if a>b and b<c and c>d:
    print('N')
elif a==b==c==d:
    print('N')
elif a<b and b>c and c<d:
    print('N')
elif a>b and b<c and c<d:
    print('N')
elif a<=b<=c<d:
    print('N')
else:
    print('S')