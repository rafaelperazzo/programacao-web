# -*- coding: utf-8 -*-
import math

n = int(input(''))
a = int(input(''))
b = int(input(''))

if a>b:
    k = 0
    m = 1
    for i in range (0,1000000,1):
        if m%a==0 or m%b==0:
            print(m)
        m += 1
        k += 1
        if k==n:
            break

if b>a:
    k = 0
    m = 1
    for i in range (a,1000000,1):
        if m%a==0 or m%b==0:
            print(m)
        m += 1
        k += 1
        if k==n:
            break