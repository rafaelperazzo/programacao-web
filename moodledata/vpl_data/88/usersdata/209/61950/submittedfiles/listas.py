# -*- coding: utf-8 -*-
def maiordegrau(a):
    x=0
    for i in range(0,len(a)-1,1):
        h=a[i]-a[(i+1)]
        if h<0:
            h=h*(-1)
        if h>x:
            x=h
    return x
lista=[]
n=int(input('Digite o tamnaho da lista:'))
for i in range(0,n,1):
    a=int(input('Digite um valor para a lista:'))
    lista.append(a)
print(maiordegrau(lista))

