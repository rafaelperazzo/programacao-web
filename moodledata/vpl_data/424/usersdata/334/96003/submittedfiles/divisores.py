# -*- coding: utf-8 -*-
import math

n = int(input(''))
a = int(input(''))
b = int(input(''))

if a>b:
    k = 0
    m = 2
    for i in range (b,999,1):
        if a%m==0 or b%m==0:
            print(m)
        m += 1
        k += 1
        if k==n:
            break

if b>a:
    k = 0
    m = 2
    for i in range (a,999,1):
        if a%m==0 or b%m==0:
            print(m)
        m += 1
        k += 1
        if k==n:
            break