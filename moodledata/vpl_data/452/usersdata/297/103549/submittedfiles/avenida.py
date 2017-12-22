# -*- coding: utf-8 -*-
m=int(input('digite o número de quadras no sentido norte-sul: '))
n=int(input('digite o número de quadras no sentido leste-oeste: '))
matriz=[]
if 2<=m and m<=1000:
    if 2<=n and n<=1000:
        for i in range(0,m,1):
            linha=[]
            for j in range(0,n,1):
                linha.append(int(input('digite o valor em milhões que a quadra possui: ')))
                while 1>matriz[i][j] or matriz[i][j]>100:
                    del matriz[i][j]
                    linha.append(int(input('digite o valor em milhões que a quadra possui: ')))
            matriz.append(linha)
        barato=0
        for i in range (0,m-1,1):
            if sum(matriz[i])<sum(matriz[i+1]):
                barato=sum(matriz[i])
            else:
                barato=sum(matriz[i+1])
    else :
        while 2>m or m>1000:
            n=int(input('digite o número de quadras no sentido leste-oeste: '))
else :
    while 2>n or n>1000:
        m=int(input('digite o número de quadras no sentido norte-sul: '))