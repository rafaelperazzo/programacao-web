# -*- coding: utf-8 -*-

def degrau(b):
    nova=[]
    d=0
    for i in range(0,len(a)-1,1):
        d=b[i]-b[i+1]
        if d<0:
            d=d*(-1)
        nova.append(d)
    return(nova)

n=int(input('Digite o tamanho da sequência:'))
a=[]
for i in range(0,n,1):
    valor=int(input('Digite os elementos da lista:'))
    a.append(valor)
    
print(degrau(a))
        

    
