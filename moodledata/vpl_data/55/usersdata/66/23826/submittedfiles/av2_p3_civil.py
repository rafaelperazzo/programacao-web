# -*- coding: utf-8 -*-
from __future__ import division

def somalinha(a,linha):
    somalinha=0
    for j in range (0,a.shape[1],1):
        somalinha=somalinha+a[linha,j]
    return somalinha
def somacoluna(a,coluna):
    somacoluna=0
    for i in range (0,a.shape[o],1):

        somacoluna=somacoluna+a[i,coluna]
    return somacoluna
def peso (a,linha,coluna):
    somatotal=somacoluna(a,coluna)+somalinha(a,linha)-(2*a[linha,coluna])
    return somatotal

n=input("digite n:")
x=input("digite o x:")
y=input("digite y:")
matriz=np.zeros((n,n))
for i in range(0,matriz.shape[0],1):
    for j in range(0,matriz.shape[1],1):
        matriz[i,j]= input("digite os elementos")
print("%.1d"%(pesso(matriz,x,y)))
