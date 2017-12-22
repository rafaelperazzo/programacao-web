# -*- coding: utf-8 -*-
import math

n = int(input(''))
a = int(input(''))
b = int(input(''))

if a>b:
    m = 2
    for i in range (b,n,1):
        if a%m==0 or b%m==0:
            print(m)
        m += 1

if b>a:
    m = 1
    for i in range (a,n,1):
        if a%m==0 or b%m==0:
            print(m)
        m += 1