# -*- coding: utf-8 -*-
import math

n=int(input('Digite n: '))
a=int(input('Digite a: '))
b=int(input('Digite b: '))

for i in range (1,n+1):
    print(a*i)
    i=i+1
    print(b*(i-1))
    i=i+1