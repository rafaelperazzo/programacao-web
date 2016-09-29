# -*- coding: utf-8 -*-
from __future__ import division
import math

a=int(input('Digite o primeiro valor: '))
b=int(input('Digite o segundo valor: '))
c=int(input('Digite o terceiro valor: '))
d=int(input('Digite o quarto valor: '))

if a==b and a==c and a==d:
    print ('N')
    
else:
    if a>b and (c<=b or c<=d) and d<=c:
        print ('S')
    
    elif (b>a and b>c) and d<=c:
        print ('S')
    
    elif a<=b and (c>b and c>d):
        print ('s')
        
    elif d>c and (b<=c and b<=a) and a<=b:
        print ('S')