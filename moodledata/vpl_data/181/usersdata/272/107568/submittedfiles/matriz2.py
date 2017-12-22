# -*- coding: utf-8 -*-
import numpy as np

n=int(input('Digite o número de elementos: '))
a=np.zeros( (n,n) )
for i in range (0,a.shape[0],1):
    for j in range (0,a.shape[1],1):
        a[i,j]=int(input('Digite o valor: '))

linha=0
coluna=0
diag_princ=0
diag_secund=0
x=0
cont=0
while(x<n):
    for k in range (0,a.shape[0],1):
        for l in range (0,a.shape[1],1):
            linha=linha+a[0,l]
            coluna=coluna+a[k,0]
            diag_princ=diag_princ+a[l,l]
            diag_secund=diag_secund+a[a.shape[0]-1-l,l]
        if (linha==coluna==diag_princ==diag_secund):
            cont=cont+1

