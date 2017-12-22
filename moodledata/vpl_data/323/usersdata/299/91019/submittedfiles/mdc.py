# -*- coding: utf-8 -*-
import math
l=[1]
x1=float(input('')) 
x2=float(input9''))
for i in range(2,x1,1):
    if x1%i==0:
        x1=x1/i
        l+=[i]
    else:
        continue
print(l)