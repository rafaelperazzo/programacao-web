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
if a<b and b>c and c<d and b<d:
    print('N')
if a==b==c<d:
    print('S')
if a>b and a==c and c==d:
    print('S')
if a==b and b==c and c>d:
    print('N')
if 
