# -*- coding: utf-8 -*-
import math

a = int(input('Digite o número 1: '))
b = int(input('Digite o número 2: '))
c = int(input('Digite o número 3: '))
d = int(input('Digite o número 4: '))
e = int(input('Digite o número 5: '))

if a > b and c and d and e:
    print(a)
elif b > a and c and d and e:
    print (b)
elif c > a and b and d and e:
    print(c)
elif d> a and b and c and e:
    print(d)
elif e > a and b and c and d:
    print(e)

elif a< b and c and d and e:
    print(a)
elif b < a and c and d and e:
    print (b)
elif c < a and b and d and e:
    print(c)
elif d< a and b and c and e:
    print(d)
elif e < a and b and c and d:
    print(e)