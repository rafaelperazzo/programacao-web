# -*- coding: utf-8 -*-
import math
a=int(input('Digite um número qualquer: '))
b=int(input('Digite um número qualquer: '))
c=int(input('Digite um número qualquer: '))
d=int(input('Digite um número qualquer: '))
if a>b and d<=c:
        print('S')
elif a<b and b>c and d<=c:
        print('S')
elif a<=b and b<c and d<c:
        print('S')
elif a<=b and b<=c and d>c:
    print('S')
else: 
    print('N')

    