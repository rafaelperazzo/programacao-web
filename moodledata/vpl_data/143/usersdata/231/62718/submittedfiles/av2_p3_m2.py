# -*- coding: utf-8 -*-
def degrau(b):
    dif=0
    degrau=0
    for j in range(0,len(b)-1,1):
        dif=b[j]-b[j+1]
        if(dif<0):
            dif=dif*(-1)
            p.append(dif)
        if (dif>degrau):
            degrau=dif
            p.append(degrau)
            
    return(degrau)
n=int(input('n:'))
a=[]
p=[]
for i in range(1,n+1,1):
    valor=int(input('valor'))
    a.append(valor)
print(degrau(a))
print(p)

def degrau(a):
    c=0
    for i range(o,len(a)-1,1):
        if a[i]>=0 and a[i+1]>=0 and a[i]>=a[i+1]:
            c=a[i]-a[i+1]
        elif a[i]>=0 and a[i+1]>=0 and a[i]<=a[i+1]:
            c=a[i+1]-a[i]
        elif a[i]>=0 and a[i+1]<0:
            c=a[i]+a[i+1]
        elif a[i]>=0 and a[i+1]>=0:
            c=a[i]+a[i+1]
    return c
n=int(input('n:'))
b=[]            
 for g in range(0,n,1):
    valor=int(input('valor'))
    b.append(valor)
print(degrau(b))
            
            
            
            
