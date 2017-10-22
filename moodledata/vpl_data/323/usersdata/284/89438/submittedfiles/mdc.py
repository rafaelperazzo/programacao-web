# -*- coding: utf-8 -*-
import math

x=int(input('digite um numero: '))
y=int(input('digite um numero: '))
n=1
while (x%n==0 and y%n==0):
    for n in range(1,x%n==0 and y%n==0,1):
        print(n)

