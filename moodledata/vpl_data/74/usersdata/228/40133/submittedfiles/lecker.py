# -*- coding: utf-8 -*-
import math
a=int(input('digite um número:'))
b=int(input('digite um número:'))
c=int(input('digite um número:'))
d=int(input('digite um número:'))
if  a<b>c>d : 
    print('S')
elif a<b>d>c:
    print('S')
elif a>b>c>d:
    print('S')
elif a<b<c>d:  
    print('S')
elif b<a<c>d: 
    print('S')
elif a<b<c<d:    
    print('S')
elif d>c>b>a:
    print('S')
else:  
    print('N')




