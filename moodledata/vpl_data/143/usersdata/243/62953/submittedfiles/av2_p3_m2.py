# -*- coding: utf-8 -*-

def degrau(m):
    valor1=[]
    c=0
    for i in range(0,len(a)-1,1):
        c=m[i]-m[i+1]
        if c<0:
            c=c*(-1)
        valor1.append(c)
    return valor1
    
n=int(input('digite o tamanho de n:'))
a=[]
for i in range(0,n,1):
    valor=int(input('digite os valores:'))
    a.append(valor)
    
print(degrau(a))    