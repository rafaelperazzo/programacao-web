# -*- coding: utf-8 -*-
import math
a=int(input('Digite um número qualquer: '))
b=int(input('Digite um número qualquer: '))
c=int(input('Digite um número qualquer: '))
d=int(input('Digite um número qualquer: '))
if a>b and a>c and a>d and b<=c and b<=d and c<=b and c<=d and d<=b and d<=c:  
    print('S')
elif b>a and b>c and b>d and a<=c and a<=d and c<=a and c<=d and d<=a and d<=c: 
    print('S')
elif c>a and c>b and c>d and a<=d and b<=a and b<=d and d<=a and d<=c: 
    print('S')
elif d>a and d>b and d>c and a<=b and a<=c and b<=a and b<=c and c<=b and c<=a:
    print('S')
else:
    print('N')
    