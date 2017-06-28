# -*- coding: utf-8 -*-
def degrau(a):
    dist=0
    degrau=0
    for i in range(0,len(a)-1,1):
        dist=a[i]-a[i+1]
        if dist<0:
            dist=dist*(-1)
        if dist>degrau:
            degrau=dist
    return (degrau)
n=int(input('Digite o tamanho da lista: '))
a=[]
for i in range(1,n+1,1):
    a.append(int(input('%dº Valor: '%i)))
print (degrau(a))

