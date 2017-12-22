# -*- coding: utf-8 -*-
import math
n=int(input(''))
a=int(input(''))
b=int(input(''))
if a>b or a==b:
    for i in range(1,n+1,1):
        x=a*i
        print(x)
else:
    for i in range(1,n+1,1):
        x=b*i
        print(x)
    

