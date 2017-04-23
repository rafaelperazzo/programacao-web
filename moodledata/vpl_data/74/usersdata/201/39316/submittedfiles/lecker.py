# -*- coding: utf-8 -*-
import math
a=int(input('Digite um número:'))
b=int(input('Digite um número:'))
c=int(input('Digite um número:'))
d=int(input('Digite um número:'))
if a<b<c<d:
    print('S')
if a==b==c==d:
    print('N')
if a==b and b<c and d==b:
    print('S')
