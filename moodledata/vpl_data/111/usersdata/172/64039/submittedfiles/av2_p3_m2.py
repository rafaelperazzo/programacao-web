# -*- coding: utf-8 -*-
import numpy as np
def le(a,b):
    lista=[]
    for i in range(0,a.shape[0],1):
        soma=0
        for j in range(0,a.shape[1],1):
            soma=soma+a[i,j]
        lista.append(soma)
    for i in range(0,len(lista),1):
        if lista[i]!=b:
            return (i)
def ce(a,b):
    lista=[]
    for j in range(0,a.shape[1],1):
        soma=0
        for i in range(0,a.shape[0],1):
            if lista[i]!=b:
                j=i
            return (j)
def l(a):
    s1=0
    s2=0
    s3=0
    for i in range(0,a.shape[0],1):
        s1=s1+a[i,0]
        s2=s2+a[i,1]
        s3=s3+a[i,2]
    if s1==s2:
        l=s1
    else:
        l=s3
    return (l)    
def vc(a,x,y,b):
    s1=0
    s2=0
    for i in range(0,a.shape[0],1):
        s1=s1+a[i,y]
    for j in range(0,a.shape[1],1):
        s2=s2+a[x,j]
    w=s1+s2-(2*a[x,y])
    v=b-(w/2)
    return (v)
n=int(input('tamanho :'))
a=np.zeros((n,n))
for i in range(0,a.shape[0],1):
    for j in range(0,a.shape[1],1):
        a[i,j]=int(input('o elemento:'))
b=l(a)        
x=le(a,b)
y=ce(a,b)
resposta=vc(a,x,y,b)
print('%.f'%a[x,y])
print('%.f'%resposta)