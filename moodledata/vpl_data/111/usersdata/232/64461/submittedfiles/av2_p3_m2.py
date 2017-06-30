# -*- coding: utf-8 -*-
import numpy as np

def M(a):
    Soma1=0
    Soma2=0
    Soma3=0
    for i in range (0,a.shape[0],1):
        Soma1=Soma1+a[i,0]
        Soma2=Soma2+a[i,1]
        Soma1==Soma2+a[i,2]
        M=Soma2
    else:
        M=Soma3
    return(M)

def LinhaE(a,M):
    l=[]
    for i in range(0,a.shape[0],1):
        soma=0
        for j in range(0,a.shape[1],1):
            soma=soma+a[i,j]
        l.append(soma)
    for i in range (0,len(l),1):
        if l[i]!=M:
            return(i)

def ColunaE(a,M):
    c=[]
    for j in range(0,a.shape[1],1):
        soma=0
        for i in range (0,a.shape[0],1):
            soma=soma+a[i,j]
            c.append(soma)
    for i in range(0,len(c),1):
        if c[i]!=M:
            j=i
        return(j)
        
def ValorC(a,x,y,m):
    soma1=0
    soma2=0
    for i in range(0,a.shape[0],1):
        soma1=soma1+a[i,y]
    for j in range (0,a.shape[1],1):
        soma2=soma2+a[x,j]
    h=soma1+soma2-(2*a[x,y])
    valor=M-(h/2)
    return(valor)

n=int(input('Digite o número de linhas e colunas da matriz: '))

a=np.zeros((n,n))
for i in range (0,a.shape[0],1):
    for j in range (0,a.shape[1],1):
        a[i,j]=int(input('Digite o elemento da matriz: '))
M=M(a)
x=LinhaE(a,M)
y=ColunaE(a,M)
ResultadoFinal=ValorC(a,x,y,M)
print('%d' %a[x,y])
print('%d' %ResultadoFinal)