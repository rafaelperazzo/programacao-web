# -*- coding: utf-8 -*-
import math
n=int(input('digite n: '))
for i in range(1,n,1):
    h=i*i
    if i%2!=0:
        imp=i/h
    if i%2==0:
        par=i/h
s=imp-par
print(s)


