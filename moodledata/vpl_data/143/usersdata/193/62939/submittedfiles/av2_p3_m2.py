# -*- coding: utf-8 -*-

def degrau(j,h):
    for i in range (0,n-1,1):
        h.append(j[i]-j[i+1])
    for i in range(0,len(b),1):
        if(h[i]<0):
                h[i]=h[i]*(-1)
    return(h)
    
n=int(input('digite a quantidade de elementos:'))
j=[]
h=[]
for i in range (0,n,1):
    valor=int(input('digite o valor da lista:'))
    a.append(valor)
print(degrau(j,h))
