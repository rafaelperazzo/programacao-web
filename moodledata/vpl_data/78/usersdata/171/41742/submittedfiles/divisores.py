# -*- coding: utf-8 -*-
import math
n=int(input('digite n:'))
a=int(input('digite a:'))
b=int(input('digite b:'))
for i in range(1,n+1,1):
    if i%a==0:
        print(i)
    if  i%b==0:
        print(i)