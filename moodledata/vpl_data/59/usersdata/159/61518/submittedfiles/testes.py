# -*- coding: utf-8 -*-
def sequencia(n):
    a=[]
    while n>0:
        x=0
        for i in range (0,n,1):
            x=x+(n-i)
        a.append(x)
        n=n-1
    return a
n=int(input('digite n:'))

print(sequencia(n))
    