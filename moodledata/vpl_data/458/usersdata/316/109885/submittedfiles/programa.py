# -*- coding: utf-8 -*-
import numpy as np
soma=o
peso=[]
while true:
    n=int(input('digite a dimensao do tabuleiro: '))
    if n>=3:
        break
dr=np.zeros((n,n))
for i in range(0,n,1):
    for j in range(0,n,1):
        dr[i,j]=int(input('digite um valor: '))
sml=0
smc=0
for i in range(0,n,1):
    for k in range(0,n,1):
        for j in range(0,n,1):
            sml=sml+dr[i,j]
            smc=smc+dr[j,k]
        sm=sml+smc-2*dr[i,k]
        peso.append(soma)
        sml=0
        smc=0
        soma=0
print((max(peso))