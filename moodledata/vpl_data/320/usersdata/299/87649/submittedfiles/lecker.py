# -*- coding: utf-8 -*-
import math
cont=0
a=int(input(''))
b=int(input(''))    
c=int(input(''))
d=int(input(''))
L=(a,b,c,d)
if n==1:
    print('N')
if L[0]>L[1]:
    cont+=1
for i in range(2,3):
    if L[i-1]<L[i] and L[i]>L[i+1]:
        cont+=1
if L[3]>L[2]:
    cont+=1
if cont>1:
    print('N')
else:
    print('S')
    