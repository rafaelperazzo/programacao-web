# -*- coding: utf-8 -*
import numpy as np
n=int(input('Digite a Dimensão da Matriz:'))
x=int(input('Digite o indice x:'))
y=int(input('Digite o indice y:'))
a=np.zeros((n,n))
for i in range(0,a.shape[0],1):
    for j in range(0,a.shape[1],1):
        a[i,j]=int(input('Digite um valor:'))
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
            if j==y:
                soma=soma+a[i,j]
    soma2=soma-a[x,y]
    return(soma2)
s1=(soma1(a))
s2=(soma2(a))
s3=s1+s2
print('%d'%s3)