# -*- coding: utf-8 -*-


def degrau(a):
    c=0
    for i range (0,len(a)-1,1):
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
            
            
            
            
