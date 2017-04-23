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
if a<b>c<d:
    print('N')
if a<b>c>d:
    print('S')
    