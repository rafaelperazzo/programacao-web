# -*- coding: utf-8 -*-
import math

a = int(input('Digite o número 1: '))
b = int(input('Digite o número 2: '))
c = int(input('Digite o número 3: '))
d = int(input('Digite o número 4: '))
e = int(input('Digite o número 5: '))

if a==b==c==d==e:
    print (a)
    print (b)
elif b==d and a==c and b>a and e<a:
    print (e)
    print (b)
elif d<a and d<b and d<c and d<e and e>b:
    print (d)
    print (e)

