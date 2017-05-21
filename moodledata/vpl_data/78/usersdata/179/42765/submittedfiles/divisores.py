# -*- coding: utf-8 -*-
import math
a=int(input('digite a:'))
b=int(input('digite b:'))
n=int(input('digite n:'))

for i in range(1,n,1):
    if i%a==0:
        print(i)
    if i%b==0:
        print(i)
    if i%a==0 and i%b==0:
        print(i)
        