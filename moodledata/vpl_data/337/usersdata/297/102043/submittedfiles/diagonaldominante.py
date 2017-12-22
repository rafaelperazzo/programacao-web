# -*- coding: utf-8 -*-
m=int(input('digite o número de linhas que a matriz possuirá: '))
n=int(input('digite o número de linhas que a matriz possuirá: '))
matriz=[]
for i in range (0,m,1):
    linha=[]
    for j in range(0,n,1):
        linha.append(int(input('digite o valor da linha%d ,coluna%d possuirá: ' %((i+1),(j+1)))))
    matriz.append(linha)
print(matriz)