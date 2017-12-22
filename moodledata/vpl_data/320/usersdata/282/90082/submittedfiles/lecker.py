# -*- coding: utf-8 -*-
import math
a = int(input('Digite o primeiro algarismo: '))
b = int(input('Digite o segundo algarismo: '))
c = int(input('Digite o terceiro algarismo: '))
d = int(input('Digite o quarto algarismo: '))
if a>b and b<=c and c<=d and d<=a:
    print('S')
elif b>a and b>c and c<=d and d<a:
    print('S')
elif c>b and c>d and d<=a and a<=b:
    print('S')
elif d>c and a<=b and b<=c and c<=d:
    print('S')
else:
    print('N')
    
   