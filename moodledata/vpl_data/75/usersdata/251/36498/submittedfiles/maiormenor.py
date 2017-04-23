# -*- coding: utf-8 -*-
import math

a = int(input('Digite o número 1: '))
b = int(input('Digite o número 2: '))
c = int(input('Digite o número 3: '))
d = int(input('Digite o número 4: '))
e = int(input('Digite o número 5: '))

#CONTINUE...
if a>b and b>c and c>d:
    print(a)
    
elif b>a and a>c and c>d:
    print(b)
    
elif c>a and a>b and b>d:
    print(c)

elif d>c and c>b and b>a:
    print(d)
