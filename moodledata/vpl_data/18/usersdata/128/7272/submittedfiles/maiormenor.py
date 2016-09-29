# -*- coding: utf-8 -*-
from __future__ import division
import math

a = input('Digite o número 1: ')
b = input('Digite o número 2: ')
c = input('Digite o número 3: ')
d = input('Digite o número 4: ')
e = input('Digite o número 5: ')

#CONTINUE...

maior=0
menor=0

if a>=b and  a>=c and a>=d and a>=e:
    maior=a
    
elif b>=a and b>=c and b>=d and b>=e:
    maior=b

elif c>=a and c>=b and c>=d and c>=e:
    maior=c
    
elif d>=a and d>=b and d>=c and d>=e:
    maior=d
    
elif e>=a and e>=b and e>=d and e>=c:
    maior=e
    
if a<=b and a<=c and a<=d and a<=e:
    menor=a

elif b<=a and b<=c and b<=d and b<=e:
    menor=b

elif c<=a and c<=b and c<=d and c<=e:
    menor=c
    
elif d<=a and d<=c and d<=b and d<=e:
    menor=d
    
elif e<=a and e<=c and e<=b and e<=d:
    menor=e

print menor
print maior 