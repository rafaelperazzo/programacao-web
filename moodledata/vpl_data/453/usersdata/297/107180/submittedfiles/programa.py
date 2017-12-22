# -*- coding: utf-8 -*-
m=int(input('digite o numero de linhas/colunas que o tabuleiro tera: '))
n=m
matriz=[]
for i in range(m):
    linha=[]
    for j in range(n):
        linha.append(int(input('digite o valor da posição de linha%d e coluna%d : '%((i+1),(j+1)))))
    matriz.append(linha)
forca_max=-1
for i in range(m):
    for j in range(n):
        posicao_torre=matriz[i][j]
        ika=j
        ak=sum(matriz[i])
        soma_coluna=-1
        for j in range(ika,ika+1,1):
            for i in range(m):
                soma_coluna=soma_coluna+matriz[i][j]
        forca=((ak-posicao_torre)+(soma_coluna-posicao_torre))
        if forca>forca_max :
            forca_max=forca
        ak=0
        posição_torre=0
print(forca_max)
        