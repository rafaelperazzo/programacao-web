# -*- coding: utf-8 -*-
import math
n=int(input('digite n:'))
i=1
num=1
den=n
termo=0
while i<=n:
    termo=termo+(num/den)
    i=i+1
    den=den-1
print('%.5f'%termo)


