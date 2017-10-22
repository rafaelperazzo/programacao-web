# -*- coding: utf-8 -*-
n=int(input(''))
cont=0
for i in range(0,n):
    t=int(input(''))
    for t in range(0,10,1):
        t1=int(input(''))
        if t1-t<10:
            continue
        else:
            cont=cont+t+t1
        
    