# -*- coding: utf-8 -*-
import math
n=int(input('digite n: '))
a=int(input('digite a: '))
b=int(input('digite b: '))
d=1
k=0
while k<n:
    if d%a==0 or d%b==0:
        print(d)
    d=d+1