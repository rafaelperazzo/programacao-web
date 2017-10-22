# -*- coding: utf-8 -*-
import math
cont=0
a=int(input(''))
b=int(input(''))    
c=int(input(''))
d=int(input(''))
L=(a,b,c,d)

#primeiros termos
if L[0]>L[1]:
    cont+=1
#termos centrais
if L[0]<L[1] and L[1]>L[2]:
    cont+=1
if L[2]>L[1] and L[2]>L[3]:
    cont+=1
#ultimos termos
if L[3]>L[2]:
    cont+=1
if cont>1 or cont==0:
    print('N')
else:
    print('S')
    