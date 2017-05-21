# -*- coding: utf-8 -*-
import math
n=float(input('Digite o valor de n:'))
s=0
for i in range(1,n+1,1):
    if i%2!=0:
        s=s+i/i*i
    else:
        s=s-i/i*i
print('%.5f'%s)

