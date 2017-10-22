# -*- coding: utf-8 -*-
import math

x=int(input('digite um numero: '))
y=int(input('digite um numero: '))
n=1
for n in range(1,x+1,1):
    if (x%n==0 and y%n==0):
        print(n)
        

