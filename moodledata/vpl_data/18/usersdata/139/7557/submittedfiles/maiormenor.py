# -*- coding: utf-8 -*-
from __future__ import division
import math

a = input('Digite o número 1: ')
b = input('Digite o número 2: ')
c = input('Digite o número 3: ')
d = input('Digite o número 4: ')
e = input('Digite o número 5: ')

#CONTINUE...
#menor
if(a<b and a<c and a<d and a<e):
    print('%.0f'%a)
    elif(b<a and b<c and b<d and b<e):
        print('%.0f'%b)
    elif(c<a and c<b and c<d and c<e):
        print('%.0f'%c)
    elif(d<a and d<b and d<c and d<e):
        print('%.0f'%d)
    elif(e<a and e<b and e<c and e<d):
        print('%.0f'%e)
#mair
if(a>b and a>c and a>d and a>e):
    print('%.0f'%a)
    elif(b>a and b>c and b>d and b>e):
        print('%,0f'%b)
    elif(c>a and c>b and c>d and c>e):
        print('%.0f'%c)
    elif(d>a and d>b and d>c and d>e):
        print('%.0f'%d)
    elif(e>a and e>b and e>c and e>d):
        print('%.0f'%e)