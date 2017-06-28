# -*- coding: utf-8 -*-

def degrau(m):
    y=[]
    x=0
    for i in range(0,len(a)-1,1):
        x=m[i]-m[i+1]
        if x<0:
            x=x*(-1)
        y.append(x)
    return nova
    
n=int(input('digite o tamanho de n:'))
a=[]
for i in range(0,n,1):
    valor=int(input('digite os valores:'))
    a.append(valor)
    
print(degrau(a))    