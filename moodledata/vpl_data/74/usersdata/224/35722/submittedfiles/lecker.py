# -*- coding: utf-8 -*-
import math
a=int(input('Digite o primeiro valor: '))
b=int(input('Digite o segundo valor: '))
c=int(input('Digite o terceiro valor: '))
d=int(input('Digite o quarto valor: '))
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
if a>b and b<c and c<d and a>d:
    print('N')
if a<b and b>c and c>d and b>d:
    print('S')
    