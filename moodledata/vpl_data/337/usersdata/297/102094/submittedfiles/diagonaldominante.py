# -*- coding: utf-8 -*-
m=int(input('digite o valor de linhas/colunas que terá a matriz: '))
n=m
matriz=[]
for i in range (0,m,1):
    linha=[]
    for j in range(0,n,1):
        linha.append(int(input('digite o valor da linha%d ,coluna%d possuirá: ' %((i+1),(j+1)))))
    matriz.append(linha)
vrd=0
for i in range(m-1,-1,-1):
    soma=0
    for j in range(n-1,-1,-1):
        print(i)
        print(j)
        if i==j :
            soma=sum(matriz[i])-matriz[i][j]
            if soma<matriz[i][j]:
                vrd=vrd+1
if vrd==n :
    print('S')
else :
    print('N')