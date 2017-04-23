# -*- coding: utf-8 -*-
import math
a = float(input('Digite o número 1:'))
b = float(input('Digite o número 2:'))
c = float(input('Digite o número 3:'))
d = float(input('Digite o número 4:'))
e = float(input('Digite o número 5:'))
if a<b and a<c and a<d and a<e and e>b and e>c and e>d:
    print(a)
    print(e)
elif -(a<b and a<c and a<d and a<e and e>b and e>c and e>d):
    print(e)
    print(a)