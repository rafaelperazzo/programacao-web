# -*- coding: utf-8 -*-
import numpy as np
n=int(input('digite a dimensão da matriz:'))
x=int(input('digite o índice x:'))
y=int(input('digite o índice y:'))
a=np.zeros((n,n))
for i in range(0,a.shape[0],1):
    for j in range(0,a.shape[1],1):
        a[i,j]=int(input('digite a:'))
def soma1(a):
    soma=0
    for i in range(0,a.shape[0],1):
        for j in range(0,a.shape[1],1):
            if i==x:
                soma=soma+a[i,j]
    soma1=soma-a[x,y]
    return(soma1)
def soma2(a):
    soma=0
    for j in range(0,a.shape[1],1):
        for i in range(0,a.shape[0],1):
            if j==x:
                soma=soma+a[i,j]
    soma2=soma-a[x,y]
    return(soma2)
s1=(soma(a))
s2=(soma(a))
s3=s1+s2
print('%d'%s3)

            
        

    

