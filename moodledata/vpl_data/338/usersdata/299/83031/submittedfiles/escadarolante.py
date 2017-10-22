# -*- coding: utf-8 -*-
n=int(input(''))
for i in range(n):
    t=int(input(''))
    for t in range(0,10,1):
        t1=int(input(''))
        if t1-t<10:
            continue
        else:
            break
    print(t+t1)    
    