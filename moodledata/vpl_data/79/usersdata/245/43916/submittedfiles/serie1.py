# -*- coding: utf-8 -*-
import math
n=int(input('Digite o valor de n:'))
s=0
x=1
while x<n:
    if x%2==0:
        s=s-(x/x*x)
    else:
        s=s+(x/x*x)
    x=x+1
print('%.5f'%s)