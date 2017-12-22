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
        eua=i
        ika=j
        soma_coluna=0
        for j in range(ika,ika+1,1):
            for i in range(eua):
                soma_coluna=soma_coluna+matriz[i][j]
        forca=(sum(matriz[i])-posicao_torre)+(soma_coluna-posicao_torre)
        if forca>forca_max :
            forca_max=forca
print(forca_max)
        