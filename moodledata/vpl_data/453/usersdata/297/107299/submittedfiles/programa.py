# -*- coding: utf-8 -*-
m=int(input('digite o numero de linhas/colunas que o tabuleiro tera: '))
n=m
matriz=[]
for i in range(0,m,1):
    linha=[]
    for j in range(0,n,1):
        linha.append(int(input('digite o valor da posição de linha%d e coluna%d : '%((i+1),(j+1)))))
    matriz.append(linha)
def soma(linha,i,j):
    p=j
    somacol=0
    for j in range(p,p+1,1):
        for i in range(0,m,1):
            somacol=somacol+matriz[j][i]
    return somacol
import soma
peso_max=0
for i in range(0,m,1):
    lin=sum(matriz[i])
    for j in range(0,n,1):
        torre=matriz[i][j]
        colunas=soma(matriz[j],j)
        forca=((lin+colunas)-(torre*2))
        print(forca)
print(peso_max)
        

        