# -*- coding: utf-8 -*-
import numpy as np
def m(a):
    somaa=0
    somb=0
    somac=0
    for i in range(0,a.shape[0],1):
        somaa=somaa+a[i,0]
        somab=somab+a[i,1]
        somac=somac+a[i,2]
    if somaa==somab:
        m=somaa
    else:
        m=somac
    return m
def linhaincorreta(a,m):
    lista=[]
    for i in range(0,a.shape[0],1):
        soma=0
        for j in range(0,a.shape[1],1):
            soma=soma+a[i,j]
        lista.append(soma)
    for i in range(0,len(lista),1):
        if lista[i]!=m:
            return(i)
def colunaincorreta(a,m):
    c=[]
    for j in range(0,a.shaoe[1],1):
        soma=0
        for i in range(a.shape[0],1):
            soma=soma+a[i,j]
            c.append(soma)
        for i in range(0,len(c),1):
            if c[i]!=m:
                j=i
            return(j)
def valorcorreto(a,x,y,m):
    somaa=0
    somab=0
    for i in range(0,a.shape[0],1):
        somaa=somaa+a[i,y]
    for j in range(a.shape[1],1):
        somab=somab+a[x,y]
    z=somaa+somab-(2*a[x,y])
    valorobtido=m-(z/2)
    return(valorobtido)
n=int(input('digite tamanho da matriz desejada:'))
mat=np.zeros((n,n))
for i in range(0,mat.shape[0],1):
    for j in range(0,mat.shape[1],1):
        mat[i,j]=int(input('digite o numero:'))
m=m(mat)
x=linhacorreta(mat,m)
y=colunaincorreta(mat,m)
res=valorcorreto(mat,x,y,m)
print('%.f'%mat[x,y])
print('%.f'%res)
            
            
