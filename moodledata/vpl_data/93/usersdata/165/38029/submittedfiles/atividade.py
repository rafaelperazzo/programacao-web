# -*- coding: utf-8 -*-
import math
n=int(input('digite um valor para n:'))

for termo in range (1,n+1,1):
    x=float(input('digite um valor para x:'))
    y=float(input('digite um valor para y:'))
    if x>=0 and y>=0 and (x**2)+(y**2)<=1:
        print(SIM)
    else:
        print(NAO)



