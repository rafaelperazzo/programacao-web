# -*- coding: utf-8 -*-
import math
n=int(input('digite n: '))
i=1
while i<=n:
    x=int(input('digite x: '))
    y=int(input('digite y: '))
    if x>=0 and y>=0 and (x*x+y*y)<=1:
        print('SIM')
    else:
        print('NAO')

