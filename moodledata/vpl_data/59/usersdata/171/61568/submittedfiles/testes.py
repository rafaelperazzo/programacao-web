# -*- coding: utf-8 -*-
import math
#COMECE AQUI ABAIXO
def soma(a,b):
    vaium=0
    c=[]
    for i in range(len(a)-1,-1,-1):
        soma=a[i]+b[i]+vaium
        if soma<10:
            c.insert(0,soma)
            vaium=0
        else:
            c.insert(0,soma%10)
            vaium=1
    if vaium==1:
        c.insert(0,1)
    return(c)
n=int(input('digite n:'))
a=[]
for i in range(0,n,1):
    valor1=float(input('digite o numero a:'))
    a.append(valor1)
m=int(input('digite m'))
b=[]
for i in range(0,m,1):
    valor2=float(input('digite o numero b:'))
    b.append(valor2)
print(soma(a,b))