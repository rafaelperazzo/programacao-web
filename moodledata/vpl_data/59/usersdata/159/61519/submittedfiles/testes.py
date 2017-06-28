# -*- coding: utf-8 -*-
def sequencia(n):
    a=[]
    while j<n:
        x=0
        for i in range (0,n,1):
            x=x+(n-i)
        a.append(x)
        j=j+1
    return a
n=int(input('digite n:'))

print(sequencia(n))
    