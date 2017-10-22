# -*- coding: utf-8 -*-
n=int(input(''))
cont=0
for i in range(n):
    if n%2==0:
        t1=int(input(''))
        t2=int(input(''))
        if t1-t2<10:
            cont=t2+10
            print(cont)    
    