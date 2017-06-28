# -*- coding: utf-8 -*-
def degrau(a):
    maior=0
    for i in range (0,len(a)-1,1):
        degrau=a[i]-a[i+1]
        if degrau<0:
            degrau=degrau*(-1)
        else:
            degrau=degrau
        if degrau>maior:
            maior=degrau
    return maior
n=int(input('tamanho da lista:'))
a=[]
for i in range (0,n,1):
    valor=int(input('valor:'))
    a.append(valor)
print(degrau(a))

