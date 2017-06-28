# -*- coding: utf-8 -*-
import math
#COMECE AQUI ABAIXO
def sub(a,b):
    c=[]
    for i in range(len(a)-1,-1,-1):
        if a[i]<b[i]:
            sub=(10+a[i])-b[i]
            c.insert(0,sub)
            a[i]=a[i]-1
        else:
            sub=a[i]-b[i]
            c.insert(0,sub)
            a[i]=a[i]
        if a[i]=len(a)-1:
            sub=a[i]-b[i]
    return(sub)
n=int(input('digite o numero:'))
a=[]
for i in range(0,n,1):
    valor1=float(input('digite numeor p/ a:'))
    a.append(valor1)
m=int(input('digite o numero:'))
b=[]
for i in range(0,m,1):
    valor2=float(input('digite numeor p/ b:'))
    b.append(valor2)