# -*- coding: utf-8 -*-
def sequencia(n):
    a=[]
    j=1
    while j<=n:
        x=0
        for i in range (0,j,1):
            x=x+(j-i)
        a.append(x)
        j=j+1
    return a
n=int(input('digite n:'))

print(sequencia(n))
    