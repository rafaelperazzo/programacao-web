# -*- coding: utf-8 -*-
def menorcoluna (a):
    for j in range (0,a.shape[1],1):
        for i in range (0,a.shape[0],1):
            if a[i,j]==1:
                return j
def menorlinha (a):
    for i in range (0,a.shape[0],1):
        for j in range (0,a.shape[1],1):
            if a[i,j]==1:
                return i
def maiorlinha (a):
    for i in range (a.shape[0]-1,-1,-1):
        for j in range (0,a.shape[1],1):
            if a[i,j]==1:
                return i
def menorcoluna (a):
    for j in range (a.shape[1]-1,-1,-1):
        for i in range (0,a.shape[0],1):
            if a[i,j]==1:
                return j
import numpy as np

a=int(input("Digite o número de linhas: "))
b=int(input("Digite o número de colunas: "))
m=np.zeros((a,b))
for i in range (0,m.shape[0],1):
    for j in range (0,m.shape[1],1):
        m[i,j]=float(input("Digit um termo: "))
z= menorlinha(m)
x= maiorlinha(m)
c= menorcoluna(m)
v= maiorcoluna(m)
print(m[z:x+1, c:v+1])