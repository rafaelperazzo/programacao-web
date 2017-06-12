# -*- coding: utf-8 -*-
a=int(input('digite a:'))
b=int(input('digite b:'))
for i in range(0,a,1):
    c=int(input('digite c:'))
    d=b-c
    while i==a:
        if d<0:
            print('N')
        elif d>=0:
            print('S')
        