# -*- coding: utf-8 -*-
import math

a = int(input('Digite o número 1: '))
b = int(input('Digite o número 2: '))
c = int(input('Digite o número 3: '))
d = int(input('Digite o número 4: '))
e = int(input('Digite o número 5: '))
if a<b and a<c and a<d and a<e and b>a and b>c and b>d and b>e:
    print('a')
    print('e')
elif a<c<d<e<b:
    print('a')
    print('b')
elif a<d<e<f<c:
    print('a')
    print('c')
else:
    if a<e<f<b<c: