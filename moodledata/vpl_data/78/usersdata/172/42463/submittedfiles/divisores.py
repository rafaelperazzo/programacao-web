# -*- coding: utf-8 -*-
import math
n=int(input('digite n: '))
a=int(input('digite a: '))
b=int(input('digite b: '))
ma=1
mb=1
for i in range(0,n,1):
    if ma==mb:
        print(ma)
        ma=ma+a
        mb=mb+b