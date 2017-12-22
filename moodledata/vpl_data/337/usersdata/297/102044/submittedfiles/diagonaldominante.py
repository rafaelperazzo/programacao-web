# -*- coding: utf-8 -*-
n=int(input('digite o número de linhas que a matriz possuirá e este equivalerá ao número de colunas: '))
m=n
matriz=[]
for i in range (0,m,1):
    linha=[]
    for j in range(0,n,1):
        linha.append(int(input('digite o valor da linha%d ,coluna%d possuirá: ' %((i+1),(j+1)))))
    matriz.append(linha)
print(matriz)
