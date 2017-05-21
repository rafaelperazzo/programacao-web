# -*- coding: utf-8 -*-
import math
n=float(input('Digite o valor de n:'))
s=0
x=1
i=1
while i<n:
    if i%2==0:
        s=s-(x/x*x)
    else:
        s=s+(x/x*x)
    x=x+1
    i=i+1
print('%.5f'%s)
