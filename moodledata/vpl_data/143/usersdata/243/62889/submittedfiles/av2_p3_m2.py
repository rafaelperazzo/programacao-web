# -*- coding: utf-8 -*-

def degrau(b):
    x=[]
    y=0
    for i in range(0,len(a)-1,1):
        d=b[i]-b[i+1]
        if y<0:
            y=y*(-1)
        x.append(y)
    return x
    
n=int(input('digite o tamanho de n:'))
a=[]
for i in range(0,n,1):
    valor=int(input('digite os valores:'))
    a.append(valor)
    
print(degrau)    