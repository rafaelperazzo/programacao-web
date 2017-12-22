# -*- coding: utf-8 -*-
import math

x=int(input('Digite o valor de x(x>0): '))
y=int(input('Digite o valor de y(y>0): '))

n=1
mdc=0

while n<=x:
    if x%n==0 and y%n==0:
        mdc = n
        print(n)
    n= n+1