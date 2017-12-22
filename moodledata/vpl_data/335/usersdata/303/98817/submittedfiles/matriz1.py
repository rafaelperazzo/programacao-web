# -*- coding: utf-8 -*-
A=[]
m=int(input('Digite a quantidade de linhas: '))
n=int(input('Digite a quantidade de colunas: '))
for i in range(0,m,1):
    for j in range(0,n,1):
        A[i][j]=int(input('Digite o termo '+str(i)+'x'+str(j)+': '))
print(A)