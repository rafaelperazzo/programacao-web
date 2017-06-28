# -*- coding: utf-8 -*-
def degrau(a):
    lista=[]
    for i in range(1,len(a),1):
        diferença=abs(a[i]-a[i+1])
        lista.append(diferença)
    return(lista)
    
def maoir(a):
    x=degrau(a)
    maior=x[0]
    for i in range(0,len(x),1):
        if x[i]>maior:
            maior=x[i]
    rturn(maior)

n=int(input('digite o tamanho da lista:'))
a=[]
for i in range(0,n,1):
    y=int(input('valor:'))
    a.append(y)
print(maior(a))