# -*- coding: utf-8 -*-
import math
a=float(input('digite a:'))
b=float(input('digite b:'))
c=float(input('digite c:'))
d=float(input('digite d:'))

if (b>a) and (b>c) and (d>c):
    print ('nao')
elif (c>b) and (c>d) and (a>b):
    print('nao')
elif (b>a) and (b>c) or ( c>b) and (c>d):
    print ('sim')
elif (a>b) and (b>c):
    print ('não')
elif (a>b) or (b>c):
    print('sim')
else:
    print('não')
    

    
