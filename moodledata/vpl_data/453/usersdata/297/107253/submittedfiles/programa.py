# -*- coding: utf-8 -*-
m=int(input('digite o numero de linhas/colunas que o tabuleiro tera: '))
matriz=[]
for i in range(m):
    linha=[]
    for j in range(m):
        linha.append(int(input('digite o valor da posição de linha%d e coluna%d : '%((i+1),(j+1)))))
    matriz.append(linha)
forca_max=-1
for i in range(0,m,1):
    al=sum(matriz[i])
    for j in range(0,m,1):
        pos_tor=matriz[i][j]
        print(pos_tor)
        ika=j
        soma_coluna=0
        for i in range(0,m,1):
            for i in range(ika,ika+1,1):
                soma_coluna=soma_coluna+matriz[i][j]
        forca=((al+soma_coluna)-(2*pos_tor))
        if forca_max<forca :
            forca_max=forca
        ak=0
        forca=0
        pos_tor=0
print(forca_max)

        