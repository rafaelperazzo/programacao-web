# -*- coding: utf-8 -*-
a=int(input('digite a:'))
b=int(input('digite b:'))
e=0
for i in range(0,a+1,1):
    c=int(input('digite c:'))
    d=int(input('digite d:'))
    if c+d>=b:
        e=e+1
    elif i==a:
        print(e)
    
    