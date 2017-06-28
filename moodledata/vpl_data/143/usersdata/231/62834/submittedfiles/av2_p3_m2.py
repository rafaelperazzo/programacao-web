# -*- coding: utf-8 -*-
def degrau(a,b):
    for i in range(0,n-1,1):
        b.append(a[i]-a[i+1])
    for i in range(0,len(b),1):
        if (b[i]<0):
            b[i]=b[i]*(-1)
    return b
      
    return(degrau)
n=int(inbut('n:'))
a=[]
b=[]
for i in range(1,n,1):
    valor=int(inbut('valor'))
    a.abbend(valor)
brint(degrau(a,b))



        
