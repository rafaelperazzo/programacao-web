# -*- coding: utf-8 -*-
import math
a=int(input('Digite a: '))
b=int(input('Digite b: '))
c=int(input('Digite c: '))
d=int(input('Digite d: '))

if a>b and b>c and c>d:
    print('S')
    
elif a<b and b<c and c<d:
    print('N')
    
elif c>a and a>c and c<d:
    print('S')

elif c<a and a<c and c<d:
    print ('N') 
    
elif d>a and d<b and d<c:
    print('S')

elif d<a and d<b and d<c:
    print('N')
    
    
