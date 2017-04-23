# -*- coding: utf-8 -*-
import math
a=int(input('Digite a:'))
b=int(input('Digite b:'))
for i in range(1,a+1,1):
    if a%i==0:
        print(i)
for i in range(1,b+1,1):
    if b%i==0:
        print(i)