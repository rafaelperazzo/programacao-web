# -*- coding: utf-8 -*-
from __future__ import division
import math

a = input('Digite o número 1: ')
b = input('Digite o número 2: ')
c = input('Digite o número 3: ')
d = input('Digite o número 4: ')
e = input('Digite o número 5: ')
maior=0
menor=0

if a>=b and >=c and a>=d and a>e :
    maior=a
    
elif a<=b and b>=c and b>=d and b>e:
    maior=b
    
elif c>=b and c>=a and c>=d and c>=e:
    maior=c

elif d>=a and d>=c and d>=b and d>=e:
    maior=d
    
elif e>=a and e>=b and e>=c and e>=d:
    maior=e
print maior
    
    