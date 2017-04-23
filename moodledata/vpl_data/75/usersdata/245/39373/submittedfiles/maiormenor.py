# -*- coding: utf-8 -*-
import math

a = int(input('Digite o número 1: '))
b = int(input('Digite o número 2: '))
c = int(input('Digite o número 3: '))
d = int(input('Digite o número 4: '))
e = int(input('Digite o número 5: '))
if a<b and a<c and a<d and a<e:
    print(a)
elif b<a and b<c and b<d and b<e:
    print(b)
elif c<a and c<b and c<d and c<e:
    print(c)
elif d<a and d<b and d<c and d<e:
    print(d)
elif a>b and a>c and a>d and a>e:
    print(a)