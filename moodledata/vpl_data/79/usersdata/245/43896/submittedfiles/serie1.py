# -*- coding: utf-8 -*-
import math
n=int(input('Digite o valor de n:'))
s=0
x=1
for i in range(1,n+1,1):
    if i%2==0:
        s=s+x/x*x
    else:
        s=s-x/x*x
    x=x+1
print('%.5f'%s)

