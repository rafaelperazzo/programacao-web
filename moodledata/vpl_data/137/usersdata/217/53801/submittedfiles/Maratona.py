# -*- coding: utf-8 -*-
a=int(input('digite a:'))
b=int(input('digite b:'))
e=0
for i in range(0,a,1):
    c=int(input('digite c:'))
    c=c+e
    d=b-c
    if d<0:
        print('N')
    elif d>=0:
        print('S')
        