# -*- coding: utf-8 -*-

def degrau(b):
    k=0
    degrau=0
    for i in range(0,len(b)-1,1):
        k=b[i]-b[i+1]
        if k<0:
            z=z*(-1)
        if k>degrau:
            degrau=k
    return(degrau)
    
n=int(input('digite a quantidade de elementos:'))
g=[]
for i in range(0,n,1):
    valor=int(input('digite o elemento:'))
    g.append(valor)
print(degrau(g))

