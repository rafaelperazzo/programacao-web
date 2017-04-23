# -*- coding: utf-8 -*-
import math

a = int(input('Digite o número 1: '))
b = int(input('Digite o número 2: '))
c = int(input('Digite o número 3: '))
d = int(input('Digite o número 4: '))
e = int(input('Digite o número 5: '))
if a>=b and a>=c and a>=d and a>=e:
    print('%f' %a)
elif b>=a and b>=c and b>=d and b>=e:
    print('%f' %b)
elif c>=a and c>=b and c>=d and c>=e:
    print('%f' %c)
elif d>=a and d>=b and d>=c and d>=e:
    print('%f' %d)
elif e>=a and e>=b and e>=c and e>=d:
    print('%.f' %e)
if a<=b and a<=c and a<=d and a<=e:
    print('%f' %a)
elif b<=a and b<=c and b<=d and b<=e:
    print('%f' %b)
elif c<=a and c<=b and c<=d and c<=e:
    print('%f' %c)
elif d<=a and d<=b and d<=c and d<=e:
    print('%f' %d)
elif e<=a and e<=b and e<=c and e<=c:
    print('%f' %e)
