# -*- coding: utf-8 -*-
import math
#COMECE AQUI ABAIXO
def sub(a,b):
    t=0
    c=[]
    for i in range(len(a)-1,-1,-1):
        sub=(t+a[i])-b[i]
        if a[i]==0: 
            if a[i]<b[i]:
                c.insert(0,sub)
                t=10
            else:
                c.insert(0,sub)
                t=0
        else:
            if a[i]<b[i]:
                sub1=(a[i]-1)-b[i]
                c.insert(0,sub1)
                t=10
            else:
                 c.insert(0,sub)
                 t=0
    if a[i]==len(a)-1:
        sub=a[i]-b[i]
        c.insert(0,sub)
    return(c)
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
print(sub(a,b))