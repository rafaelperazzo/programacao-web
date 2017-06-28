# -*- coding: utf-8 -*-
import numpy as np
def M(a):
    s1=0
    s2=0
    s3=0
    for i in range (0,a.shape[0],1):
        s1=s1+a[i,0]
        s2=s2+a[i,1]
        s1=s3+a[i,2]
    if s1==s2:
        M=s1
    else:
        M=s3    
    return(M)
def L_errada(a,M):
    lista=[]
    for i in range (0,a.shape[0],1):
        s=0
        for j in range (0,a.shape[1],1):
            s=s+a[i,j]
        lista.append(s)
    for i in range (0,len(lista),1):
        if lista[i]!=M:
            return (i)
def C_errada(a,M):
    lista=[]
    for j in range (0,a.shape[1],1):
        s=0
        for i in range (0,a.shape[1],1):
            s=s+a[i,j]
        lista.append(s)
    for i in range (0,len(lista),1):
        if lista[i]!=M:
            j=i
        return (j)
def certo(a,x,y,M):
    s1=0
    s2=0
    for i in range (0,a.shape[0],1):
        s1=s1+a[i,y]
    for j in range (0,a.shape[1],1):
        s2=s2+a[x,j]
    z=s1+s2-(2*a[x,y])
    valor=M-(z/2)
    return (valor)
    
n=int(input('tamanho da matriz:'))
m=np.zeros((n,n))
for i in range (0,m.shape[0],1):
    for j in range (0,m.shape[1],1):
        m[i,j]=int(input('elementos:'))
M=M(m)
x=L_errada(m,M)
y=C_errada(m,M)
result=certo(m,x,y,M)
print('%.f'%m[x,y])
print('%.f'%result)
        

