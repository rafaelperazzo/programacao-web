# -*- coding: utf-8 -*-
import math
n=int(input('digite n: '))
a=int(input('digite a: '))
b=int(input('digite b: '))
d=1
for i in range(1,n,1):
    if a%d==0 and b%d==0:
        d=d+1
        print(d)
