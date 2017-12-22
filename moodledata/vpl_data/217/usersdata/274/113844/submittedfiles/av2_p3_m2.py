# -*- coding: utf-8 -*
import numpy as np

Dim=int(input("Dimensão da matriz: "))
x=int(input("Quantidade de linhas: "))
y=int(input("Quantidade de colunas: "))
a=np.zeros((Dim,Dim))

for m in range (0,DIM,1):
    for n in range (0,Dim,1):
        a[m,n]=int(input("Elemento da matris: "))

def SL (M,IL):
    soma=0
    for n in range (0,M.shape[1],1):
        soma=soma+M[IL,n]

def SC (M,IC):
    soma=0
    for m in range (0,M.shape[0],1):
        soma=soma+M[m,IC]

R=SL(a,x)+SC(a,y)-(2*a[x,y])
print ("%d" %R)

   