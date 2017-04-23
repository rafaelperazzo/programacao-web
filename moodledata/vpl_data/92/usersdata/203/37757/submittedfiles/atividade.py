# -*- coding: utf-8 -*-
import math
n=int(input('digite n: '))
num=1
den=n
i=1
S=num/den
while i>n:
    num=num+1
    den=n-1
    S=S+(num/den)
    i=i+1
print('%.5f'%S)