# -*- coding: utf-8 -*-
import math
a=int(input('Digite o valor: '))
b=int(input('Digite o valor: '))
c=int(input('Digite o valor: '))
d=int(input('Digite o valor: '))
if a==c and b!=d:
    print('V')
elif b==d and a!=c:
    print('V')
else:
    print('F')
