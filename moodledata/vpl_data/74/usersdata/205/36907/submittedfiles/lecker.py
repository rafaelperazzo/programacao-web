# -*- coding: utf-8 -*-
import math
a=float(input('digite a:'))
b=float(input('digite b:'))
c=float(input('digite c:'))
d=float(input('digite d:'))

if (b>a) and (b>c) and (d>c):
    print ('n')
elif (c>b) and (c>b) and (a>b):
    print('n')
elif (b>a) and (b>c) or ( c>b) and (c>d):
    print ('s')
elif (a>b) and (d>c):
    print ('n')
elif (a>b) or (d>c):
    print('s')
else:
    print('n')
    

    
