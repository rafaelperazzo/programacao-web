# -*- coding: utf-8 -*-
import math
n=int(input('Digite n: '))
a=int(input('Digite a: '))
b=int(input('Digite b: '))
mult=1
cont=0
for cont in range(1,n+1,1):
    if mult%a==0 or mult%b==0:
        print(mult)
    mult=mult+1
    
