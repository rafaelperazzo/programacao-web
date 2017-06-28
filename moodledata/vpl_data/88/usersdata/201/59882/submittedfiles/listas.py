# -*- coding: utf-8 -*-
def degrau(b):
    x=[]
    for i in range(0,len(b)1,1):
        diferença=abs(b[i]-b[i+1])
        x.append(diferença)
    return(x)
    
def maior(d):
    c=degrau(b)
    maior=c[0]
    for i in range(0,len(c),1):
        if c[i]>maior:
            maior=c[i]
    return(maior)
    
n=int(input('lista:'))
d=[]
for i in range(1,n+1,1):
    r=int(input('valor:'))
    d.append(r)
print(maior(d))
    
    
