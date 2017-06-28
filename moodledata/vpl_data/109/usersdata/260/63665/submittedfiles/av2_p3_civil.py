# -*- coding: utf-8 -*-
import numpy as np

def linha (n,t):
    soma=0
    for i in range (0,t.shape[1],1):
        soma=soma+t[n,1]
    return (soma)
def coluna (n,t):
    soma=0
    for i in range (0,t.shape[1],1):
        soma=soma+m[1,n]
    return (soma)

d=int(input("digite o valor da dimenão:"))
linha=int(input("digite a linha desejada"))
coluna=int(input("digite a coluna desejada"))
matriz=np.zeros( (d,d) )
for i in range (0,matriz.shape[0],1):
    for j in range (0,matriz.shape[1],1):
        matriz[i,j]=float(input("digite o elemento da matriz requerido"))
valor=(linha(linha,coluna)+coluna(linha,coluna)-(2*matriz[linha,coluna]))
