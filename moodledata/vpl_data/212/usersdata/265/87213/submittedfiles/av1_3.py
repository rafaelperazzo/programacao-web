# -*- coding: utf-8 -*-
import math
a = int(input('digite o valor de a: '))
b = int(input('digite o valor de b: '))
c = int(input('digite o valor de c: '))
for i in range (2,a+1,1):
    if a%i==0:
        da=i
        print(da)
        break
for j in range (2,b+1,1):
    if b%j==0:
        db=j
        print(db)
        break
for k in range (2,c+1,1):
    if c%k==0:
        dc=k
        print(dc)
        break
if di