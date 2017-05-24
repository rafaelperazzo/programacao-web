# -*- coding: utf-8 -*-
import math
m = int(input('Digite m:'))
i=2
s=3
for t in range (1,m+1,1):
    if t%2==0:
        s=s-(4/(i*(i+1)*(i+2)))
    else:
        s=s+(4/(i*(i+1)*(i+2)))
    i=i+2
print('%.6f'%s)
