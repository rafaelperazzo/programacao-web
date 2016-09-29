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

if a>=b<=c<=d<=e:
    maior=a
    
elif a<=b>=c<=d<=e:
    maior=b
    
elif a<=b<=c>=d<=e:
    maior=c

elif a<=b<=c<=d>=e:
    maior=d
    
else:
    maior=e


if a<=b>=c>=d>=e:
    menor=a
elif a>=b<=c>=d>=e:
    menor=b
elif a>=b>=c<=d>=e:
    menor=c
elif a>=b>=c>=d<=e:
    menor=d
else:
    menor=e
print menor 
print maior
    
    