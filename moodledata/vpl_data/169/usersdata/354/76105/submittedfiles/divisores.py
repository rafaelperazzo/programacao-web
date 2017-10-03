# -*- coding: utf-8 -*-
import math

n=int(input('digite o n: '))
a=int(input('digite o a (a>0): '))
b=int(input('digite o b (b>0): '))
#PROCESSAMENTO
mult=0
k=0
while (k>n):
    if mult%a==0 or mult%b==0:
        print(mult)
        k=k+1
    mult=mult+1
    
