# -*- coding: utf-8 -*-
import math
a=int(input('Digite a: '))
b=int(input('Digite b: '))
c=int(input('Digite c: '))
d=int(input('Digite d: '))

if a>b and a>c and a>d:
    print('S')

elif b>a and b>c and b>d:
    print('S')
    
elif c>a and c>b and c>d:
    print('S')
    
elif d>a and d>b and d>c:
    print('S')
    
else:
    if a<b and a<c and a<d:
        print('N')
    
    elif b<a and b<c and b<d:
        print('N')
        
    elif c<a and c<b and c<d:
        print('N')
        
    elif d<a and d<b and d<c:
        print('N')
    
    else:
        if  a==b==c==d:
            print('N')