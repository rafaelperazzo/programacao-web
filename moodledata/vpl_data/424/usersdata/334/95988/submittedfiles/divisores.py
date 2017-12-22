# -*- coding: utf-8 -*-
import math

n = int(input(''))
a = int(input(''))
b = int(input(''))

k = 0
if a>b:
    m = 2
    for i in range (b,n,1):
        if a%m==0 or b%m==0:
            print(m)
        m += 1
        k += k
        if k==n:
            break

if b>a:
    m = 2
    for i in range (a,n,1):
        if a%m==0 or b%m==0:
            print(m)
        m += 1
        k += k
        if k==n:
            break