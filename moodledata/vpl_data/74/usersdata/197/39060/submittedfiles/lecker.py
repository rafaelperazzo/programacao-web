# -*- coding: utf-8 -*-
import math
a=int(input('Digite o valor do número a:'))
b=int(input('Digite o valor do número b:'))
c=int(input('Digite o valor do número c:'))
d=int(input('Digite o valor do número d:'))
if a<b<c<d and a<b>c>d and a<=b<c>d and a<=b<=c<d:
    print('S')
else:
    print('N')