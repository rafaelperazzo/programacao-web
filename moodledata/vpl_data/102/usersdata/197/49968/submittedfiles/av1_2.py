# -*- coding: utf-8 -*-
import math
a=int(input('Digite o valor de a:'))
b=int(input('Digite o valor de b:'))
c=int(input('Digite o valor de c:'))
d=int(input('Digite o valor de d:'))
if a==c and b!=d:
    print('V')
elif a!=c and b==d:
    print('V')
else:
    print('N')