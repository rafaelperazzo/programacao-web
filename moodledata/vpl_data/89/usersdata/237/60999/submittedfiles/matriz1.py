# -*- coding: utf-8 -*-
import numpy as np
a=int(input("Digite o número de linhas: "))
b=int(input("Digite o número de colunas: "))
m=np.zeros((a,b))
for i in range (0,m.shape[0],1):
    for j in range (0,m.shape[1],1):
        m[i,j]=float(input("Digit um termo: "))
print(m)
e=0
f=0
g=0
h=0
for i in range (0,m.shape[0],1):
    for j in range (0,m.shape[1],1):
        if m[i,j] != 0:
            e=e+i
        break
for i in range (0,m.shape[0],1):
    for j in range (0,m.shape[1],1):
        if m[i,j] != 0:
            f=f+i
for j in range (0,m.shape[1],1):
    for i in range (0,m.shape[0],1):
        if m[i,j] != 0:
            g=g+j
        break
for j in range (0,m.shape[1],1):
    for i in range (0,m.shape[0],1):
        if m[i,j] != 0:
            h=h+j
print(m[(e-1):(f-1),(g-1):(h-1)])