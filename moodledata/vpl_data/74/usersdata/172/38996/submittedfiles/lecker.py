# -*- coding: utf-8 -*-
import math
a=int(input('digite um valor:'))
b=int(input('digite um valor:'))
c=int(input('digite um valor:'))
d=int(input('digite um valor:'))
if  a<b<c<d or a>b>c>d or a>b<c>d or a<b>c>d or a>=b<c>d or a==b==c>d:
    print('S')
else:
    print('N')