# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np
def colunadi(a):
    direita=0
    for i in range(0,a.shape[0],1):
        for j in range(0,a.shape[1],1):
            if a[i,j]==1:
                if j>=direita:
                    direita=j
    return direita
def colunaesq(a):
    esquerda=a.shape[0]-1
    for i in range(0,a.shape[0],1):
        for j in range(0,a.shape[1],1):
            if a[i,j]==1:
                if j<=esquerda:
                    esquerda=j
    return esquerda
def linhabaixo(a):
    baixo=0
    for i in range(0,a.shape[0],1):
        for j in range(0,a.shape[1],1):
            if a[i,j]==1:
                if i>=baixo:
                    baixo=i
    return baixo
def linhacima(a):
    alto=a.shape[1]-1
    for i in range(0,a.shape[0],1):
        for j in range(0,a.shape[1],1):
            if a[i,j]==1:
                if i<=alto:
                    alto=i
    return alto
n=input('digite a quantidade de linhas:')
m=input('digite a quantidade de colunas:')
a=np.zeros((n,m))
for i in range(0,a.shape[0],1):
    for j in range(0,a.shape[1],1):
        a[i,j]=input('digite o elemento:')
x=colunadi(a)
y=colunaesq(a)
z=linhabaixo(a)
t=linhacima(a)
print(a[t:z+1,y:x+1])