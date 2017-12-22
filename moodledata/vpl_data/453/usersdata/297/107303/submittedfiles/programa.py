# -*- coding: utf-8 -*-
m=int(input('digite o numero de linhas/colunas que o tabuleiro tera: '))
n=m
matriz=[]
for i in range(0,m,1):
    linha=[]
    for j in range(0,n,1):
        linha.append(int(input('digite o valor da posição de linha%d e coluna%d : '%((i+1),(j+1)))))
    matriz.append(linha)
def soma(matriz,i,j):
    somacol=0
    for j in range(p,p+1,1):
        for i in range(0,m,1):
            somacol=somacol+matriz[i][j]
    return somacol
peso_max=0
for i in range(0,m,1):
    lin=sum(matriz[i])
    for j in range(0,n,1):
        torre=matriz[i][j]
        p=j
        colunas=soma(matriz,m,p)
        forca=((lin+colunas)-(torre*2))
        print(forca)
print(peso_max)
        

        