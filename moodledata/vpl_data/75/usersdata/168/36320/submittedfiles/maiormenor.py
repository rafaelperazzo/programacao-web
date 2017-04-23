# -*- coding: utf-8 -*-
import math

a = int(input('Digite o número 1: '))
b = int(input('Digite o número 2: '))
c = int(input('Digite o número 3: '))
d = int(input('Digite o número 4: '))
e = int(input('Digite o número 5: '))
if (a>b) and (a>c):
    print(a)
elif (b>a) and (b>c):
    print(b)
else:
    print(c)
    if (a<b) and (a<c):
        print(a)
    elif (b<a) and (b<c):
        print(b)
    else:
        print(c)