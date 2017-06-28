# -*- coding: utf-8 -*-

def maior(a):
    g=0
    maior=0
    for i in range(0,len(a)-1,1):
        
        g=a[i]-a[i+1]
        if g<0:
            g=g*(-1)
        if g>maior:
            maior=g
    return(maior)
        
n=int(input('digite o total de números:'))
x=[]

for i in range(0,n,1):
    d=int(input('digite os elementos:'))
    x.append(d)
print(maior(x))

