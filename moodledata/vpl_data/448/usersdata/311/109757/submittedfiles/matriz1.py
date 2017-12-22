# -*- coding: utf-8 -*-
m=int(input('Digite o numero de linhas: '))
n=int(input('Digite o numero de colunas: '))
mat=[]
for i in range (0,m,1):
    a=[]
    for j in range (0,n,1):
        a.append(' ')
    mat.append(a)
for i in range (m-1,-1,-1):
    for j in range (n-1,-1,-1):
        mat[i][j]=int(input('Digite o numero: '))
print (mat)
    

