# -*- coding: utf-8 -*-
n=int(input(''))
cont=0
t=int(input(''))
if n==1:
    cont=t+10
    print(cont)
elif n>1:
    for t in range(n):
        t1=int(input(''))
        if t1-t<10:
            cont=cont+t1+t+10
            continue
        elif t1-t>=10:
            cont=t1+10+t+10
            continue
        break
    print(cont)
        
    