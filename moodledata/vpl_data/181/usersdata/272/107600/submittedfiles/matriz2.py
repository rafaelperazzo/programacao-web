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
            linha=linha+a[x,l]
            coluna=coluna+a[k,x]
            diag_princ=diag_princ+a[x,x]
            diag_secund=diag_secund+a[a.shape[0]-1-x,x]
        if ((linha==coluna) and (linha==diag_princ) and (linha==diag_secund) and (coluna==diag_princ) and (coluna==diag_secund) and (diag_princ==diag_secund)):
            cont=cont+1
    x=x+1

if cont==n:
    print('S')
else:
    print('N')

