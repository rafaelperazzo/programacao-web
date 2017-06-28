# -*- coding: utf-8 -*-
import numpy as np
def descobrirm(a):
    s1=0
    s2=0
    s3=0
    for i in range(0,a.shape[0],1):
        s1=s1+a[i,0]
        s2=s2+a[i,1]
        s3=s3+a[i,2]
    
    if s1==s2:
        return(s1)
    else:
        return(s3)
        
def somalinhaerrada(a,m):
    b=[]
    for i in range(0,a.shape[0],1):
        soma=0
        for j in range(0,a.shape[1],1):
            soma=soma+a[i,j]
        b.append(soma)
    
    for r in range(0,len(b),1):
        if b[i]!=m:
            return i
def somacolunaerrada(a,m):
    b=[]
    for j in range(0,a.shape[1],1):
        soma=0
        for i in range(0,a.shape[0],1):
            soma=soma+a[i,j]
        b.append(soma)
    
    for j in range(0,len(b),1):
        if b[j]!=m:
            return j
            
            
def numero_original(m,x,y,a):
    s1=0
    s2=0
    for i in range(0,a.shape[0],1):
        s1=s1+a[i,y]
    for j in range(0,a.shape[1],1):
        s2=s2+a[x,j]
        
    z=s1+s2-(2*a[x,y])
    valorcerto=m-(z/2)
    return valorcerto
    
    
n=int(input('digite a dimensao da matriz:'))
a=np.zeros((n,n))
for i in range(0,a.shape[0],1):
    for j in range(0,a.shape[1],1):
        a[i,j]=int(input('digite o numero:'))

m=descobrirm(a)        
x=somalinhaerrada(a,m)
y=somacolunaerrada(a,m)
resultado=numero_original(m,x,y,a)
print('%.f'%a[x,y])
print('%.f'%resultado)
        
