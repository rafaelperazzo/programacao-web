# -*- coding: utf-8 -*-

def maior(a):
    for i in range(lend(a)-1,0,-1):
        g=a-a[i]
        
        if g<0:
            g==g*(-1)
        return(g)
        
n=int(input('digite o total de números:'))
x=[]

for i in range(0,n,1):
    d=int(input('digite os elementos:'))
    x.append(d)
print(maior(x))

