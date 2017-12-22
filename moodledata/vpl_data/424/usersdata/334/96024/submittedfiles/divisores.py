# -*- coding: utf-8 -*-
import math

n = int(input(''))
a = int(input(''))
b = int(input(''))

if a>b:
    m = 1
    for i in range (b,6,1):
        if m%a==0 or m%b==0:
            print(m)
        m += 1

if b>a:
    m = 1
    for i in range (a,6,1):
        if m%a==0 or m%b==0:
            print(m)
        m += 1