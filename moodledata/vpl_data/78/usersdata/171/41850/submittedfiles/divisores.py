# -*- coding: utf-8 -*-
import math
n=int(input('digite n:'))
a=int(input('digite a:'))
b=int(input('digite b:'))
mult=0
c=0
while c<n:
    if mult%a==0 or mult%b==0:
        c+c+1
        print(mult)
    