# -*- coding: utf-8 -*-
def degrau(l1):
    dif=0
    degrau=0
    for i in range(0,len(l1)-1,1):
        dif=l1[i]=l1[i+1]
        if (dif<0):
            dif=dif*(-1)
        if (dif>degrau):
            degrau=dif
    return(degrau)

n=int(input('Digite o Valor de Elementos da Lista'))
l1=[]
for i in range(1,n+1,1):
    v=int(input('Digite os Elementos da Lista:'))
    l1.append(v)
print(degrau(l1))

