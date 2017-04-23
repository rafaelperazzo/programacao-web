# -*- coding: utf-8 -*-
import math
n=int(input('digite n: '))
num=1
den=n
S=num/den
while num<=n:
    S=S+(num/den)
    num=num+1
    den=n-1
print('%.5f'%S)