# -*- coding: utf-8 -*-
import math
a=int(input('Digite o primeiro número:  '))
b=int(input('Digite o segundo número:   '))
c=int(input('Digite o terceiro número:  '))
d=int(input('Digite o quarto número:    '))
if (a<b) and (b<c) and (c<d):
    print('S')
elif a==b and a==c and a==d:
    print('N')
elif a<b and b>c and c<d:
    print('N')
elif a<b and b>c and c>d:
    print('S')
elif a==b and b<c and a==d:
    print('S')