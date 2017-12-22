# -*- coding: utf-8 -*-

impot numpy as np

Dim=int(input("Dimensão da matriz: "))
x=int(input("Quantidade de linhas: "))
y=int(input("Quantidade de colunas: "))
a=np.zeros((Dim,Dim))

for i in range (0,Dim,1):
    for j in range (0,Dim,1):
        a[i,j]=int(input("Elemento da Matriz: "))

def SL (M,IL):
    soma=0
    for j in range (0,M.shape[1],1):
        soma=soma+M[IL,j]

def SC (M,IC):
    soma=0
    for i in range (0,M.shape[0],1):
        soma=soma+M[i,IC]

R=SL(a,x)+SC(a,y)-(2*a[x,y])
print ("%d" %R)

