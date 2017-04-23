# -*- coding: utf-8 -*-
import math
a=int(input('Digite um número qualquer: '))
b=int(input('Digite um número qualquer: '))
c=int(input('Digite um número qualquer: '))
d=int(input('Digite um número qualquer: '))
if a>b and b>c and c>d:
    print('S')
elif d>c and c>b and b>a:
    print('S')
    
else: 
    print('N')
    