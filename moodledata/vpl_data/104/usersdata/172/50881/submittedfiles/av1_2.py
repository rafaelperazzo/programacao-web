# -*- coding: utf-8 -*-
import math
n=int(input('digite n'))
l1=int(input('digite l1: '))
c1=int(input('digite c1: '))
l2=int(input('digite l2: '))
c2=int(input('digite c2: '))
c=n/2
if l1<=c and c1<=c and l2<=c and c2<=c:
    print('N')
elif l1>c and c1>c and l2>c and c2>c:
    print('N')
elif l1>c and c1<=c and l2>c and c2<=c:
    print('N')    
elif l1<=c and c1>c and l2<=c and c2>c:
    print('N')    
else :
    print('S')
    
    