# -*- coding: utf-8 -*-
import math

a = int(input('Digite o número 1: '))
b = int(input('Digite o número 2: '))
c = int(input('Digite o número 3: '))
d = int(input('Digite o número 4: '))
e = int(input('Digite o número 5: '))

#CONTINUE...
if a>b and b>c and c>d and d>e:
    print(a)
    
elif b>a and a>c and c>d and d>e:
    print(b)
    
elif c>a and a>b and b>d and d>e:
    print(c)

elif d>c and c>b and b>a and d>e:
    print(d)
    
elif e>a and a>b and b>c and c>d:
    print(e)
