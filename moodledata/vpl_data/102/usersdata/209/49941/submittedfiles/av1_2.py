# -*- coding: utf-8 -*-
import math
a=int(input('Digite o primeiro número:'))
b=int(input('Digite o segundo número:'))
c=int(input('Digite o terceiro número:'))
d=int(input('Digite o quarto número:'))
if a==c and a!=b and a!=d and b!=d:
    print('V')
elif b==d and a!=b and a!=c and b!=c:
    print('V')
else:
    print('F')