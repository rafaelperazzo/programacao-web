# -*- coding: utf-8 -*-
n=int(input(''))
cont=0
t=int(input(''))
if n==1:
    cont=t+10
    print(cont)
elif n>1:
    for i in range(n):
        t=int(input(''))
        i=10+t
    print(i)
    