# -*- coding: utf-8 -*-

def degrau(a):
    l=[]
    menos=0
    for i in range(0,len(a)-1,1):
        if a[i]<0:
            a[i]=a[i]*(-1)
            menos=menos+(a[i]-a[i+1])
            menos.append[l]
        if a[i]>=0:
            menos=menos+(a[i]-a[i+1])
            l.append[menos]
    
    for i in range(0,len(l)-1,1):
        maior=0
        if l[i]>l[i+1]:
            maior=a[i]
            return(a[i])
a=[]
n=int(input('Digite o tamanho da lista:'))
for i in range(0,n,1):
    x=int(input('Digite o numero:'))
    a.append(x)

print(degrau(a))
    
            
            
