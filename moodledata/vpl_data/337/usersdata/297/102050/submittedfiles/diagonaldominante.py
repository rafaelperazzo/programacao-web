# -*- coding: utf-8 -*-
n=int(input('digite o número de linhas que a matriz possuirá e este equivalerá ao número de colunas: '))
m=n
matriz=[]
for i in range (0,m,1):
    linha=[]
    for j in range(0,n,1):
        linha.append(int(input('digite o valor da linha%d ,coluna%d possuirá: ' %((i+1),(j+1)))))
    matriz.append(linha)
vrd=0
for i in range(0,m,1):
    j=0
    soma=0
    soma=sum(matriz[i])-matriz[i][j]
    j=j+1
    if soma>matriz[i][j]:
        vrd=vrd+1
    else :
        break
if vrd==n :
    print('S')
else :
    print('N')
