# -*- coding: utf-8 -*-
import math
a=int(input('Digite o primeiro valor:'))
b=int(input('Digite o segundo valor:'))
c=int(input('Digite o terceiro valor:'))
d=int(input('Digite o quarto valor:'))
if (a>b>c>d) or (a<b>c>d) or (a<b<c>d) or (a<b<c<d) or (a>b==c==d) or (a==b==c<d) or (a==b==d and c>a) or (a==c==d and a>b):
    print('S')
else:
    print('N')