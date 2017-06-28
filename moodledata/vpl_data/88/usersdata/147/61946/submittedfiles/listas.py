# -*- coding: utf-8 -*-
def degrau(a):
    l=[]
    for i in range(0,len(a)-1,1):
        diff=abs(a[i]-a[i+1])
        l.append(diff)
    return(l)
def maior(a):
    x=degrau(a)
    maior=x[0]
    for i in range(0,len(x),1):
        if x[i]>maior
        maior=x[i]
    return(maior)
n=int(input('tamanho:'))
a=[]
for i in range(1,n+1,1):
    y=int(input('valor:'))
    a.append(y)
print(maior(a))

