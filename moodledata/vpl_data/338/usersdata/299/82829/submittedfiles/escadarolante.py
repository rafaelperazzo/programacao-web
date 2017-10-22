# -*- coding: utf-8 -*-
n=int(input(''))
t=0
x=0
for i in range(n):
    t1=int(input(''))
    if t1-t<=10:
        t=int(input(''))
    else:
        x=t1+t
    print(x)    
    